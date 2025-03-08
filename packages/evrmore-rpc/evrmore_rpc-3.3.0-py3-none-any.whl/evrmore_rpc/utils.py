"""
Utility functions for evrmore-rpc
"""

from typing import Any, Dict, List, Optional, Type, TypeVar, Union, Callable, Awaitable, Generic, Tuple
from pydantic import BaseModel
from decimal import Decimal
import json
import inspect
import asyncio
from functools import wraps, lru_cache
import threading
import aiohttp
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time
from datetime import datetime, timedelta

T = TypeVar('T', bound=BaseModel)
R = TypeVar('R')  # Return type

# Thread-local storage to track context
_context = threading.local()

def format_amount(value: Union[int, float, str]) -> Decimal:
    """Format a numeric value as a Decimal."""
    return Decimal(str(value))

def validate_response(response: Any, model: Type[T]) -> T:
    """
    Validate a response against a Pydantic model.
    
    Args:
        response: The response to validate
        model: The Pydantic model to validate against
        
    Returns:
        The validated model instance
    """
    if isinstance(response, model):
        return response
    
    return model.model_validate(response)

def validate_list_response(response: Any, model: Type[T]) -> List[T]:
    """
    Validate a list response against a Pydantic model.
    
    Args:
        response: The list response to validate
        model: The Pydantic model to validate against
        
    Returns:
        A list of validated model instances
    """
    if not isinstance(response, list):
        raise ValueError(f"Expected list, got {type(response)}")
    
    return [validate_response(item, model) for item in response]

def validate_dict_response(response: Any, model: Type[T]) -> Dict[str, T]:
    """
    Validate a dictionary response against a Pydantic model.
    
    Args:
        response: The dictionary response to validate
        model: The Pydantic model to validate against
        
    Returns:
        A dictionary of validated model instances
    """
    if not isinstance(response, dict):
        raise ValueError(f"Expected dict, got {type(response)}")
    
    return {key: validate_response(value, model) for key, value in response.items()}

def format_command_args(*args: Any) -> List[str]:
    """Format command arguments for RPC calls."""
    formatted_args = []
    for arg in args:
        if arg is None:
            continue
        if isinstance(arg, bool):
            formatted_args.append("true" if arg else "false")
        elif isinstance(arg, (dict, list)):
            # Convert to JSON string and properly escape quotes
            formatted_args.append(json.dumps(arg))
        else:
            formatted_args.append(str(arg))
    return formatted_args

def set_async_context(is_async: bool) -> None:
    """
    Set the current context as async or sync.
    
    Args:
        is_async: Whether the current context is async
    """
    _context.is_async = is_async

def is_async_context() -> bool:
    """
    Check if the current context is async.
    
    Returns:
        True if the current context is async, False otherwise
    """
    # First, check if we've explicitly set the context
    if hasattr(_context, 'is_async'):
        return _context.is_async
    
    # Otherwise, try to detect based on the current coroutine
    try:
        # If we're in a coroutine, we're in an async context
        asyncio.get_running_loop()
        return True
    except RuntimeError:
        # If we're not in a coroutine, we're in a sync context
        return False

def detect_async_context() -> bool:
    """Detect if the current execution context is asynchronous.
    
    This function inspects the call stack to determine if it's being called
    from an asynchronous context (i.e., from within a coroutine function).
    
    Returns:
        True if the current context is asynchronous, False otherwise
    """
    try:
        # Get the current call stack
        frame = inspect.currentframe()
        
        # Walk up the call stack to find any async function
        while frame:
            if inspect.iscoroutinefunction(frame.f_code):
                return True
            frame = frame.f_back
        
        # Check if we're in an active event loop
        try:
            loop = asyncio.get_running_loop()
            return True
        except RuntimeError:
            # No running event loop
            pass
        
        return False
    finally:
        # Ensure the frame reference is cleared to avoid memory leaks
        del frame

class AwaitableResult:
    """
    A special result type that can be used both with and without await.
    
    This class allows creating objects that work seamlessly in both
    synchronous and asynchronous contexts without requiring explicit
    context managers or cleanup.
    """
    
    def __init__(self, sync_result: Any, async_coro: Awaitable[Any], cleanup_func=None):
        """
        Initialize the awaitable result.
        
        Args:
            sync_result: The result to return in synchronous context
            async_coro: The coroutine to await in asynchronous context
            cleanup_func: Optional function to call for cleanup when used synchronously
        """
        self._sync_result = sync_result
        self._async_coro = async_coro
        self._cleanup_func = cleanup_func
        self._used = False
        
    def __await__(self):
        """
        Make the object awaitable.
        This is called when the object is used with 'await'.
        """
        self._used = True
        return self._async_coro.__await__()
    
    def __getattr__(self, name):
        """
        Forward attribute access to the sync result.
        This allows using the object directly as if it were the sync result.
        """
        # Mark as used in sync mode
        if not self._used:
            self._used = True
            # Cancel the coroutine to prevent warnings
            if hasattr(self._async_coro, 'close'):
                self._async_coro.close()
            elif hasattr(self._async_coro, 'cancel'):
                self._async_coro.cancel()
        
        return getattr(self._sync_result, name)
    
    def __getitem__(self, key):
        """
        Forward item access to the sync result.
        This allows using the object with dictionary-like syntax.
        """
        # Mark as used in sync mode
        if not self._used:
            self._used = True
            # Cancel the coroutine to prevent warnings
            if hasattr(self._async_coro, 'close'):
                self._async_coro.close()
            elif hasattr(self._async_coro, 'cancel'):
                self._async_coro.cancel()
        
        return self._sync_result[key]
    
    def __str__(self):
        """Return string representation of the sync result."""
        # Mark as used in sync mode
        if not self._used:
            self._used = True
            # Cancel the coroutine to prevent warnings
            if hasattr(self._async_coro, 'close'):
                self._async_coro.close()
            elif hasattr(self._async_coro, 'cancel'):
                self._async_coro.cancel()
        
        return str(self._sync_result)
    
    def __repr__(self):
        """Return representation of the sync result."""
        # Mark as used in sync mode
        if not self._used:
            self._used = True
            # Cancel the coroutine to prevent warnings
            if hasattr(self._async_coro, 'close'):
                self._async_coro.close()
            elif hasattr(self._async_coro, 'cancel'):
                self._async_coro.cancel()
        
        return repr(self._sync_result)
    
    def __del__(self):
        """Clean up resources when the object is garbage collected."""
        # If we have a cleanup function and the object was used in sync mode
        if self._cleanup_func and self._used:
            try:
                self._cleanup_func()
            except Exception:
                pass
        
        # Cancel the coroutine if it wasn't awaited
        if not self._used:
            if hasattr(self._async_coro, 'close'):
                self._async_coro.close()
            elif hasattr(self._async_coro, 'cancel'):
                self._async_coro.cancel()

def sync_or_async(sync_func: Callable[..., R], async_func: Callable[..., Awaitable[R]]) -> Callable[..., Union[R, Awaitable[R]]]:
    """
    Create a function that can be used in both sync and async contexts.
    
    Args:
        sync_func: The synchronous implementation
        async_func: The asynchronous implementation
        
    Returns:
        A function that will use the appropriate implementation based on context
    """
    @wraps(async_func)
    def wrapper(*args: Any, **kwargs: Any) -> Union[R, Awaitable[R]]:
        # Check if we're in an async context
        if is_async_context():
            return async_func(*args, **kwargs)
        else:
            return sync_func(*args, **kwargs)
    
    return wrapper 

class ConnectionPoolManager:
    """Manages HTTP connection pools for both synchronous and asynchronous clients.
    
    This class provides connection pooling, automatic retries, and timeouts
    for both synchronous and asynchronous HTTP requests.
    """
    
    def __init__(
        self,
        max_connections: int = 10,
        max_keepalive: int = 5,
        retry_total: int = 3,
        retry_backoff_factor: float = 0.5,
        timeout: float = 30.0
    ):
        """Initialize the connection pool manager.
        
        Args:
            max_connections: Maximum number of connections in the pool
            max_keepalive: Maximum number of keepalive connections
            retry_total: Maximum number of retries
            retry_backoff_factor: Backoff factor for retries
            timeout: Request timeout in seconds
        """
        self.max_connections = max_connections
        self.max_keepalive = max_keepalive
        self.retry_total = retry_total
        self.retry_backoff_factor = retry_backoff_factor
        self.timeout = timeout
        
        # Synchronous session
        self._sync_session = None
        
        # Asynchronous session
        self._async_session = None
        
    def get_sync_session(self) -> requests.Session:
        """Get or create a synchronized session with retry logic.
        
        Returns:
            A requests.Session object with connection pooling and retry logic
        """
        if self._sync_session is None:
            retry_strategy = Retry(
                total=self.retry_total,
                backoff_factor=self.retry_backoff_factor,
                status_forcelist=[429, 500, 502, 503, 504],
                allowed_methods=["HEAD", "GET", "POST", "PUT", "DELETE", "OPTIONS", "TRACE"]
            )
            
            adapter = HTTPAdapter(
                max_retries=retry_strategy,
                pool_connections=self.max_connections,
                pool_maxsize=self.max_connections,
                pool_block=True
            )
            
            session = requests.Session()
            session.mount("http://", adapter)
            session.mount("https://", adapter)
            
            self._sync_session = session
            
        return self._sync_session
    
    async def get_async_session(self) -> aiohttp.ClientSession:
        """Get or create an asynchronous session.
        
        Returns:
            An aiohttp.ClientSession object with connection pooling
        """
        if self._async_session is None or self._async_session.closed:
            timeout = aiohttp.ClientTimeout(total=self.timeout)
            connector = aiohttp.TCPConnector(
                limit=self.max_connections,
                limit_per_host=self.max_keepalive,
                enable_cleanup_closed=True
            )
            
            self._async_session = aiohttp.ClientSession(
                connector=connector,
                timeout=timeout,
                raise_for_status=False
            )
            
        return self._async_session
    
    async def close_async_session(self):
        """Close the asynchronous session if it exists."""
        if self._async_session and not self._async_session.closed:
            await self._async_session.close()
            self._async_session = None
    
    def close_sync_session(self):
        """Close the synchronous session if it exists."""
        if self._sync_session:
            self._sync_session.close()
            self._sync_session = None
    
    async def close(self):
        """Close all sessions."""
        await self.close_async_session()
        self.close_sync_session()
    
    def __del__(self):
        """Ensure proper cleanup when the object is garbage collected."""
        if self._sync_session:
            self.close_sync_session()
        
        # We can't use await in __del__, so we have to just close without waiting
        if self._async_session and not self._async_session.closed:
            self._async_session.connector.close()

# Global connection pool manager instance
connection_pool = ConnectionPoolManager() 

class CacheEntry(Generic[T]):
    """A cache entry with expiration time."""
    
    def __init__(self, value: T, ttl: int):
        """Initialize a cache entry.
        
        Args:
            value: The value to cache
            ttl: Time to live in seconds
        """
        self.value = value
        self.expiry = time.time() + ttl
    
    def is_expired(self) -> bool:
        """Check if the cache entry has expired.
        
        Returns:
            True if the entry has expired, False otherwise
        """
        return time.time() > self.expiry

class BlockchainCache:
    """Cache manager for blockchain data.
    
    This class provides caching for frequently accessed blockchain data
    with configurable TTL (time to live) per cache type.
    """
    
    def __init__(self):
        """Initialize the blockchain cache."""
        # Default TTLs for different types of data (in seconds)
        self.ttl = {
            'block': 60 * 10,         # 10 minutes
            'transaction': 60 * 5,     # 5 minutes
            'blockchaininfo': 60,      # 1 minute
            'networkinfo': 60 * 2,     # 2 minutes
            'asset': 60 * 5,           # 5 minutes
            'mempool': 30,             # 30 seconds
            'default': 60              # 1 minute default
        }
        
        # The actual cache storage
        self._cache: Dict[str, Dict[str, CacheEntry]] = {
            'block': {},
            'transaction': {},
            'blockchaininfo': {},
            'networkinfo': {},
            'asset': {},
            'mempool': {},
            'default': {}
        }
        
        # Lock for thread safety
        self._lock = threading.RLock()
    
    def get(self, cache_type: str, key: str) -> Optional[Any]:
        """Get a value from the cache.
        
        Args:
            cache_type: The type of cache (block, transaction, etc.)
            key: The cache key
            
        Returns:
            The cached value or None if not found or expired
        """
        if cache_type not in self._cache:
            cache_type = 'default'
        
        with self._lock:
            if key in self._cache[cache_type]:
                entry = self._cache[cache_type][key]
                if not entry.is_expired():
                    return entry.value
                
                # Remove expired entry
                del self._cache[cache_type][key]
        
        return None
    
    def set(self, cache_type: str, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """Set a value in the cache.
        
        Args:
            cache_type: The type of cache (block, transaction, etc.)
            key: The cache key
            value: The value to cache
            ttl: Optional TTL override in seconds
        """
        if cache_type not in self._cache:
            cache_type = 'default'
        
        if ttl is None:
            ttl = self.ttl.get(cache_type, self.ttl['default'])
        
        with self._lock:
            self._cache[cache_type][key] = CacheEntry(value, ttl)
    
    def invalidate(self, cache_type: Optional[str] = None, key: Optional[str] = None) -> None:
        """Invalidate cache entries.
        
        Args:
            cache_type: Optional cache type to invalidate, or all if None
            key: Optional key to invalidate, or all in the cache type if None
        """
        with self._lock:
            if cache_type is None:
                # Invalidate all caches
                for cache in self._cache.values():
                    cache.clear()
            elif key is None:
                # Invalidate a specific cache type
                if cache_type in self._cache:
                    self._cache[cache_type].clear()
            else:
                # Invalidate a specific key in a specific cache type
                if cache_type in self._cache and key in self._cache[cache_type]:
                    del self._cache[cache_type][key]
    
    def cleanup(self) -> None:
        """Remove all expired entries from the cache."""
        now = time.time()
        
        with self._lock:
            for cache_type, cache in self._cache.items():
                expired_keys = [k for k, v in cache.items() if v.is_expired()]
                for key in expired_keys:
                    del cache[key]

# Global cache instance
blockchain_cache = BlockchainCache()

def cached(cache_type: str, key_func: Optional[Callable] = None, ttl: Optional[int] = None):
    """Decorator for caching function results.
    
    Args:
        cache_type: The type of cache to use
        key_func: Optional function to generate the cache key from the function arguments
        ttl: Optional TTL override in seconds
        
    Returns:
        A decorator that caches the result of the function
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Generate the cache key
            if key_func is not None:
                cache_key = key_func(*args, **kwargs)
            else:
                # Default key is the function name + args + kwargs
                arg_str = ','.join(str(a) for a in args[1:])  # Skip self
                kwarg_str = ','.join(f"{k}={v}" for k, v in sorted(kwargs.items()))
                cache_key = f"{func.__name__}({arg_str},{kwarg_str})"
            
            # Check if the result is in the cache
            cached_result = blockchain_cache.get(cache_type, cache_key)
            if cached_result is not None:
                return cached_result
            
            # Not in cache, call the function
            result = func(*args, **kwargs)
            
            # Store the result in the cache
            blockchain_cache.set(cache_type, cache_key, result, ttl)
            
            return result
        
        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            # Generate the cache key
            if key_func is not None:
                cache_key = key_func(*args, **kwargs)
            else:
                # Default key is the function name + args + kwargs
                arg_str = ','.join(str(a) for a in args[1:])  # Skip self
                kwarg_str = ','.join(f"{k}={v}" for k, v in sorted(kwargs.items()))
                cache_key = f"{func.__name__}({arg_str},{kwarg_str})"
            
            # Check if the result is in the cache
            cached_result = blockchain_cache.get(cache_type, cache_key)
            if cached_result is not None:
                return cached_result
            
            # Not in cache, call the function
            result = await func(*args, **kwargs)
            
            # Store the result in the cache
            blockchain_cache.set(cache_type, cache_key, result, ttl)
            
            return result
        
        # Choose the wrapper based on whether the function is async
        if inspect.iscoroutinefunction(func):
            return async_wrapper
        return wrapper
    
    return decorator 
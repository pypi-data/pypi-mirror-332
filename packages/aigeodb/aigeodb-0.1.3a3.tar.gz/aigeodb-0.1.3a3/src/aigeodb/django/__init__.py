from django.apps import AppConfig
from django.core.cache import cache
from threading import local
import logging

from ..core.database import DatabaseManager

logger = logging.getLogger(__name__)


class AigeoDBConfig(AppConfig):
    name = 'aigeodb.django'
    verbose_name = 'AigeoDB'
    
    def ready(self):
        """
        Initialize the application when Django starts.
        This method is called once the registry is fully populated.
        """
        try:
            # Check cache availability
            has_cache = (hasattr(cache, 'get') and hasattr(cache, 'set'))
            cache_backend = cache if has_cache else None
            
            # Initialize database manager if not exists
            if not hasattr(self, '_db'):
                self._db = DatabaseManager()
                if cache_backend:
                    logger.info(
                        "AigeoDB: Cache backend detected and configured"
                    )
                else:
                    logger.info(
                        "AigeoDB: No cache backend available"
                    )
                
            # Make database manager thread-local
            thread_local = local()
            thread_local.db = self._db
            
            logger.info(
                "AigeoDB: Django integration initialized successfully"
            )
            
        except Exception as e:
            logger.error(
                f"AigeoDB: Failed to initialize Django integration: {e}"
            )
            raise


default_app_config = 'aigeodb.django.AigeoDBConfig'
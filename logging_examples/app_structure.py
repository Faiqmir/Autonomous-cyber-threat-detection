import logging
import sys
import structlog
import uuid
import time
import random

# Configure structured logging
def configure_logging():
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.dev.set_exc_info,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer()
        ],
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )

log = structlog.get_logger()

def simluate_user_activity():
    """Simulates a user login flow with structured logs."""
    request_id = str(uuid.uuid4())
    # Bind context variables (e.g. Request ID) to all subsequent logs in this context
    structlog.contextvars.bind_contextvars(request_id=request_id)

    user_id = f"user_{random.randint(1000, 9999)}"
    ip_address = f"192.168.1.{random.randint(1, 255)}"

    log.info("user_login_attempt", 
             user_id=user_id, 
             ip=ip_address, 
             event_category="authentication", 
             action="login")

    # Simulate success or failure
    if random.random() > 0.2:
        log.info("user_login_success", 
                 user_id=user_id, 
                 event_category="authentication", 
                 status="success")
        
        # Simulate accessing a resource
        log.info("resource_access",
                 user_id=user_id,
                 resource="/api/v1/sensitive-data",
                 method="GET",
                 status=200)
    else:
        log.warning("user_login_failed", 
                    user_id=user_id, 
                    ip=ip_address, 
                    event_category="authentication", 
                    reason="invalid_credentials",
                    status="failed")

    # Unbind context for next iteration (if this were a real server loop)
    structlog.contextvars.unbind_contextvars('request_id')

if __name__ == "__main__":
    configure_logging()
    print("Starting App with Structured Logging...")
    for _ in range(5):
        simluate_user_activity()
        time.sleep(0.5)

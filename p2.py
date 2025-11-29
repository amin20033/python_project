#  q2. Write a program to log all user activities using Python’s logging module.
import logging

def setup_logger():
    logger = logging.getLogger("activity_logger")
    logger.setLevel(logging.INFO)

    # Formatter for both handlers
    fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    # File handler (writes to user_activity.log)
    fh = logging.FileHandler("user_activity.log")
    fh.setFormatter(fmt)
    logger.addHandler(fh)

    # Console handler (prints to terminal)
    ch = logging.StreamHandler()
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    return logger

def main():
    logger = setup_logger()
    logger.info("Activity Logger started.")

    try:
        while True:
            activity = input("Enter user activity (or type 'exit' to stop): ").strip()
            if activity.lower() == "exit":
                logger.info("User exited the application.")
                break
            if activity == "":
                # ignore empty input but show helpful message
                logger.info("Empty input (no activity entered).")
                continue
            logger.info(f"User did: {activity}")

    except KeyboardInterrupt:
        logger.info("Application interrupted with Ctrl+C")
    finally:
        logger.info("Activity Logger stopped.")

if __name__ == "__main__":
    main()

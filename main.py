import threading
import time
from concurrent.futures import ThreadPoolExecutor
from message_queue import MessageQueue

def process_message(message):
    print(f"Processed message: {message}")
    message_lower = message.lower()
    
    if "high priority" in message_lower:
        result = sum(range(100))
        print(f"Sum of first 100 numbers for '{message}': {result}")
    elif "medium priority" in message_lower:
        result = sum([x*x for x in range(10)])
        print(f"Sum of squares of first 10 numbers for '{message}': {result}")
    elif "low priority" in message_lower:
        result = sum(range(5))
        print(f"Sum of first 5 numbers for '{message}': {result}")
    else:
        print(f"No specific action for '{message}'. Just logging.")

def enqueue_messages(message_queue, messages):
    for message, priority in messages:
        print(f"Enqueuing: {message} with priority {priority}")
        message_queue.enqueue_message(message, priority)
        time.sleep(1)

def dequeue_and_process_messages(message_queue, executor):
    while not message_queue.is_empty():
        message = message_queue.dequeue_message()
        executor.submit(process_message, message)

def main():
    message_queue = MessageQueue()
    
    messages_producer1 = [("Producer 1 - High priority", 1), ("Producer 1 - Medium priority", 2)]
    messages_producer2 = [("Producer 2 - Medium priority", 2), ("Producer 2 - Low priority", 3)]
    
    producer_thread1 = threading.Thread(target=enqueue_messages, args=(message_queue, messages_producer1))
    producer_thread2 = threading.Thread(target=enqueue_messages, args=(message_queue, messages_producer2))
    
    producer_thread1.start()
    producer_thread2.start()
    
    producer_thread1.join()
    producer_thread2.join()
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        dequeue_and_process_messages(message_queue, executor)

if __name__ == "__main__":
    main()

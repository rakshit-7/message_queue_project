Multi-Threaded Priority Message Queue System
This is a multi-threaded priority message queue system where multiple threads can send messages to each other with varying priorities. Upon receiving a message, the receiving thread performs a simple action using a thread pool.

Setup
Clone the Repository:git clone <(https://github.com/rakshit-7/message_queue_project.git)>
Install Dependencies:
Ensure you have Python installed on your system. This project uses standard Python libraries and does not require additional dependencies.

Execution
To run the message queue system, follow these steps:

Run the Main Script: python main.py

Usage
Upon execution, the main script (main.py) enqueues messages from multiple producers into a priority message queue and processes them using a thread pool.
The MessageQueue class in message_queue.py provides the functionality for managing the message queue, including enqueuing, dequeuing, peeking at the top message, and checking if the queue is empty.
Messages are processed based on their priority:
High priority messages: Calculate the sum of the first 100 numbers.
Medium priority messages: Calculate the sum of squares of the first 10 numbers.
Low priority messages: Calculate the sum of the first 5 numbers.
Messages are printed to the console along with the results of their processing.
Contributing
Contributions are welcome! If you have any suggestions, bug fixes, or feature implementations, please open an issue or create a pull request.
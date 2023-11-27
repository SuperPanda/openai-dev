# Plan

## Current Focus

The immediate focus is to develop TerminalAI, an AI-powered conversation management system. This project aims to create an application that enables seamless interactions with the OpenAI API, facilitating the management of conversations between users and AI assistants. The initial tasks involve creating assistants, managing threads, and implementing the functionalities to send, receive, and store messages.

The tasks will be performed within the context of the following feature scope:

1. Creating AI-powered Assistants
2. Managing Conversational Threads
3. Sending and Receiving Messages
4. Storing Messages as Files
5. Monitoring Conversations and Managing Assistant Responses

We will focus on getting parts to run in a terminal application. As well as generate a layer that will allow external applications to interface with the system.

## Development Plan

## Appendix

```
class AssistantManager:
    def __init__(self, assistant_id):
        self.assistant_id = assistant_id
        # Additional assistant-related logic and operations

class ThreadManager:
    def __init__(self, assistant_manager, thread_id):
        self.assistant_manager = assistant_manager
        self.thread_id = thread_id
        # Additional thread-related logic and operations

    def send_message(self, message):
        # Logic for sending a message using the OpenAI assistant

    def receive_message(self):
        # Logic for receiving a response message from the OpenAI assistant

class MessageManager:
    def save_message(self, thread_id, sender, content):
        # Logic to save the message as a file with a timestamp and metadata

class MessageWatcher:
    def __init__(self, folder_path):
        self.message_folder = folder_path
        # Logic to watch the message folder and process new messages
```

```
openai_mvp_project/
    |-- main.py
    |-- app/
        |-- __init__.py
        |-- assistant_manager.py
        |-- thread_manager.py
        |-- message_manager.py
        |-- message_watcher.py
```

```
@startuml
class AssistantManager
class ThreadManager
class MessageManager
class MessageWatcher

AssistantManager "1..*" - "0..*" ThreadManager
ThreadManager "1" - "0..*" MessageManager
MessageWatcher --> MessageManager
@enduml
```

```
@startuml
package "OpenAI App" {
  [main.py]
  [assistant_manager.py]
  [thread_manager.py]
  [message_manager.py]
  [message_watcher.py]
}
@enduml
```

```
@startuml
actor User
User -> ThreadManager: SendMessage(message)
ThreadManager -> ThreadManager: ReceiveMessage()
ThreadManager -> MessageManager: SaveMessage(message)
MessageManager -> MessageWatcher: UpdateFolder()
@enduml
```

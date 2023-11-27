# TerminalAI: Conversaional Intelligence for the Command Line

## Project Description

TerminalAI is a conversational intelligence application designed to bring powerful AI capabilities to the command line interface. It allows users to seamlessly interact with the OpenAI API, enabling real-time conversations with AI assistants and efficient retrieval of information using natural language queries. By leveraging the power of AI, TerminalAI transforms the command line into an intelligent assistant, providing instant access to a wealth of knowledge and the ability to execute complex tasks using simple commands.

TerminalAI can be used in the following ways:

    1. Real-time Conversations: Users can initiate and engage in real-time conversations with AI assistants directly from the command line. By running the appropriate commands, users can send messages, receive AI-generated responses, and have the conversation displayed in real-time.
    2. Information Retrieval: TerminalAI allows users to effortlessly retrieve information by posing natural language queries. Users can enter queries in plain language and obtain accurate and relevant responses from AI-powered models.
    3. Task Execution: TerminalAI can execute a wide range of tasks through conversations with AI assistants. By interacting with the assistants, users can perform actions such as file operations, data analysis, and more, all from the convenience of the command line.

Current Development Iteration

At the completion of the current development iteration, TerminalAI will provide the following functionalities:

    1. Users can run the ./send-message script to send messages and view them in real-time using the ./listen script.
    2. Messages sent by users will be saved as files in the designated thread folder and can be displayed in the ./listen terminal.
    3. TerminalAI will integrate with the OpenAI API to process user messages and provide AI-generated responses.
    4. Conversations and AI-generated replies will be displayed in real-time, allowing for interactive and dynamic conversations from the command line.

This iteration prioritizes real-time message exchange and basic AI integration, ensuring an initial usable version of TerminalAI.

Please refer to the development plan outlined in PLAN.md for more details on the project's roadmap and upcoming iterations.

With TerminalAI, command line users can benefit from the power of AI to improve their productivity, retrieve information, and perform a wide range of tasks. The completion of the current development iteration brings us one step closer to realizing this vision, with real-time conversations and AI integration at the forefront. Let's continue our journey to enhance the command line experience with the intelligence of TerminalAI.

## TerminalAI Development Plan

### Task Breakdown

To ensure incremental progress and usability at every stage, here is a task breakdown in order of importance for developing TerminalAI, a conversational intelligence application for the command line.
Task 1: Initial Setup

    [ ] Initialize the project structure and version control with Git.
    [ ] Set up the initial main script and shell commands for managing conversations.

Task 2: Sending and Saving Messages

    [ ] Implement the functionality to send user messages and save them as files in the designated thread folder.
    [ ] Create a file watch system to monitor the message folder and display updates in real-time.

Task 3: AI Assistant Integration

    [ ] Integrate the OpenAI API to process user messages and receive AI-generated responses.
    [ ] Implement the logic to store AI-generated responses as message files in the thread folder.

Task 4: Thread and Assistant Management

    [ ] Add support for creating and switching between different threads within the application.
    [ ] Implement the ability to manage multiple AI assistants and switch between them as needed.

Task 5: Message Display and Retrieval

    [ ] Develop the functionality to display messages from the message files in the terminal.
    [ ] Implement the ability to retrieve and display previous messages in the conversation.

Note: The tasks are listed in order of importance, allowing for incremental progress with usable features at every stage. Dependencies between tasks may exist but are generally minimized for flexibility.

## First time

TODO: setup.py {develop,install} will be configured at some point. And an executable with options parsing and help menus

```
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip (?)
pip install -r requirements.txt
```

## setup-tmux.zsh

```
├── Window: Development
│   └── Horizontal Split
│       ├── Vertical Split
│       │   ├── Pane: Code (nvim)
│       │   └── Pane: Shell (clear)
│       └── Vertical Split
│           ├── Pane: Documentation (most README.md)
│           └── Pane: Git Log (watch -n 1 'git --no-pager log --color=always -n 1 -p')
└── Window: OpenAI Assistant Integration
    └── Horizontal Split
        ├── Pane: Settings (clear)
        └── Horizontal Split
            ├── Vertical Split
            │   ├── Pane: Chat History (clear)
            │   └── Pane: Chat Input Controls (clear)
            └── Pane: Logs
```

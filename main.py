"""
    TerminalAI: Conversaional Intelligence for the Command Line

    TerminalAI is a conversational intelligence application designed to bring powerful AI capabilities to the command line interface. It allows users to seamlessly interact with the OpenAI API, enabling real-time conversations with AI assistants and efficient retrieval of information using natural language queries. By leveraging the power of AI, TerminalAI transforms the command line into an intelligent assistant, providing instant access to a wealth of knowledge and the ability to execute complex tasks using simple commands.

    usage: ./main.py [send MSG [THREAD] [--assistant=ASSISTANT] [--model=MODEL] | listen [--thread THREAD] | modify [assistant=ASSISTANT] [--model=MODEL]  [--thread=thread] | show [models | assistants | threads ] 
"""

import argparse

parser = argparse.ArgumentParser(description="TerminalAI: Conversaional Intelligence for the Command Line")
parser.add_argument("--version",action="version",version="TerminalAI 0.1")
parser.add_argument("--debug",help="print debug messages",action="store_true")

subparser = parser.add_subparsers(title="subcommands",help="subcommand help",description="subcommand help")
send_parser = subparser.add_parser("send",help="send a message to an assistant")

send_parser.add_argument("msg",type=str,help="message to send")
send_parser.add_argument("--thread",type=str,help="thread to send message to")
send_parser.add_argument("--assistant",type=str,help="assistant to use")
send_parser.add_argument("--model",type=str,help="model to use")

listen_parser = subparser.add_parser("listen",help="listen to an assistant")
listen_parser.add_argument("--thread",type=str,help="thread to listen to")

modify_parser = subparser.add_parser("modify",help="modify an assistant")
modify_parser.add_argument("--assistant",type=str,help="assistant to modify")
modify_parser.add_argument("--model",type=str,help="model to use")
modify_parser.add_argument("--thread",type=str,help="thread to listen to")

show_parser = subparser.add_parser("show",help="list assistants, threads, or models")
show_parser.add_argument("entity",type=str,help="entity to show", choices=["models","assistants","threads"])

def main():
    args = parser.parse_args()
    print(args)
    if 'send':
        print("send: Not yet implemented")
    elif 'listen' in args:
        print("listen: Not yet implemented")
    elif 'modify' in args:
        print("modify: Not yet implemented")
    elif 'show' in args:
        print("show: Not yet implemented")
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()

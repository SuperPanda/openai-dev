# openai-dev

Software to integrate OpenAI as a developers assistant.

## First time

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

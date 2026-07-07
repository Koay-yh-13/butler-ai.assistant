# butler-ai.assistant
# Butler

Butler is a local AI desktop assistant for Windows powered by OpenRouter.

## Vision

Butler is designed to be an intelligent desktop assistant capable of:

- Natural language conversations
- Launching and managing Windows applications
- File management
- Browser automation
- Windows settings control
- Voice interaction
- Local memory
- System monitoring
- Plugin support
- Confirmation before risky actions

All automation is executed locally on your own computer.

---

## Features (Planned)

- OpenRouter integration
- Modern React interface
- FastAPI backend
- Windows automation
- Local memory
- Voice input/output
- Plugin architecture
- Task planner
- Tool calling
- Multi-step execution
- Live system monitoring
- Screen understanding (optional)

---

## Tech Stack

### Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- Framer Motion

### Backend

- Python 3.12+
- FastAPI
- WebSockets
- OpenRouter API

### Windows Automation

- pywinauto
- psutil
- pyautogui
- keyboard
- mouse
- PowerShell

---

## Repository Structure

```
Butler/
│
├── backend/
├── frontend/
├── plugins/
├── memory/
├── logs/
├── config/
├── docs/
├── installer/
│
├── run.bat
├── installer.bat
└── README.md
```

---

## Development Goals

### Version 0.1

- Backend server
- Frontend dashboard
- OpenRouter connection
- Chat interface

### Version 0.2

- Open applications
- Close applications
- File explorer

### Version 0.3

- Windows settings
- Browser control

### Version 0.4

- Memory
- Planner
- Tool calling

### Version 0.5

- Voice mode

### Version 0.6

- Plugin system

### Version 1.0

Complete AI desktop assistant.

---

## Security

Every potentially destructive action must require explicit user confirmation.

Examples:

- Delete files
- Shutdown
- Restart
- Registry edits
- PowerShell execution
- Installing software
- Network configuration

---

## License

This project is intended for personal and educational use.

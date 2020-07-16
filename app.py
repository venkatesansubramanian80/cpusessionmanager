from flask import Flask
import libtmux as lbtmux

app = Flask(__name__)


def get_new_window():
    server = lbtmux.Server()
    new_session = server.new_session(session_name="Multi_While_Session")
    new_window = new_session.new_window(window_name="Milti_While_Window", attach=False)
    return new_window


def get_new_window_More_CPU():
    server = lbtmux.Server()
    new_session = server.new_session(session_name="Multi_While_Session_More")
    new_window = new_session.new_window(window_name="Milti_While_Window_More", attach=False)
    return new_window


def get_session_More():
    server = lbtmux.Server()
    exist_session = server.find_where({"session_name": "Multi_While_Session_More"})
    return exist_session


def get_session():
    server = lbtmux.Server()
    exist_session = server.find_where({"session_name": "Multi_While_Session"})
    return exist_session


def remove_session():
    current_session = get_session()
    current_session.kill_window("Milti_While_Window")
    current_session.kill_session()


def run_application():
    new_window = get_new_window()
    command = "while true; do echo hello; sleep .01; done"
    new_window.select_pane('0').send_keys(command, enter=True)


def run_application_more():
    new_window = get_new_window_More_CPU()
    command = "while true; do echo hello; sleep .005; done"
    new_window.select_pane('0').send_keys(command, enter=True)


def remove_session_more():
    current_session = get_session_More()
    current_session.kill_window("Milti_While_Window_More")
    current_session.kill_session()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/run_application')
def application():
    try:
        run_application()
        return "success"
    except:
        return "failure"


@app.route('/kill_application')
def kill():
    try:
        remove_session()
        return "success"
    except:
        return "failure"


@app.route('/run_application_more')
def application_more():
    try:
        run_application_more()
        return "success"
    except:
        return "failure"


@app.route('/kill_application_more')
def kill_more():
    try:
        remove_session_more()
        return "success"
    except:
        return "failure"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

from flask import Flask
import libtmux as lbtmux

app = Flask(__name__)


def get_new_window():
    server = lbtmux.Server()
    new_session = server.new_session(session_name="Multi_While_Session")
    new_window = new_session.new_window(window_name="Milti_While_Window", attach=False)
    return new_window


def get_session():
    server = lbtmux.Server()
    exist_session = server.find_where({"session_name": "Multi_While_Session"})
    return exist_session


def remove_session():
    current_session = get_session()
    current_session.kill_window("Milti_While_Window")


def run_application():
    new_window = get_new_window()
    command = "while true; do echo hello; done"
    new_window.select_pane('0').send_keys(command, enter=True)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/run_application')
def application():
    run_application()
    return "success"


@app.route('/kill_application')
def kill():
    remove_session()
    return "success"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

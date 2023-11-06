from app.asistencia import bp
from flask import render_template, request, Response
import cv2
from pyzbar.pyzbar import decode

def gen_frames():
    cap = cv2.VideoCapture(1)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            for code in decode(frame):
                data = code.data.decode('utf-8')
                print(data)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@bp.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@bp.route('/control')
def control():
    return render_template("index.html")

@bp.route('/asistencia')
def asistencia():
    return render_template("asistenciaUI.html")

@bp.route('/tomarAsistencia', methods=['GET', 'POST'] )
def tomarAsistencia():
    if request.method == 'POST':
        print("Something else")
    return render_template("tomarAsistencia.html")

@bp.route('/entrega')
def entrega():
    return render_template("index.html")


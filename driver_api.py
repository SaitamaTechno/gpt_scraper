from flask import Flask, request, jsonify
import sys, time, json
import sql1

app = Flask(__name__)

# Replace 'your_api_key' with the actual API key you want to use
valid_api_key = sys.argv[1]
print(valid_api_key)
@app.route("/")
def main():
    return jsonify({"system": "Send GET request to http://127.0.0.1:80/api?api_key=saitamatechno&msg=hello"})
@app.route('/api', methods=['GET'])
def api():
    # Check if the 'api_key' parameter is provided in the request
    api_key = request.args.get('api_key')
    msg = request.args.get('msg')

    # Verify if the provided API key matches the valid API key
    if api_key == valid_api_key:
        # If the API key is valid, respond with a success message
        if msg!="" and msg!=None:
            f=open("/headless/gpt/webdriver_status.txt", "r")
            webdriver_status=f.read()
            f.close()
            # Commands for controlling the webdriver
            if msg=="!start":
                if webdriver_status=="on":
                    response = {'system': webdriver_status, 'message': "Webdriver is ready!"}
                    return json.dumps(response, ensure_ascii=False)
                elif webdriver_status=="off":
                    f=open("/headless/gpt/webdriver_status.txt", "w")
                    f.write("processing")
                    f.close()
                    response = {'system': webdriver_status, 'message': "Webdriver is starting, please wait and refresh the page!"}
                    return json.dumps(response, ensure_ascii=False)                
                elif webdriver_status=="processing":
                    response = {'system': webdriver_status, 'message': "Starting webdriver is still in progress, please wait!"}
                    return json.dumps(response, ensure_ascii=False)
                else:
                    response = {'system': webdriver_status, 'message': webdriver_status}
                    return json.dumps(response, ensure_ascii=False)
            if webdriver_status=="off":
                response = {'system': webdriver_status, 'message': "Webdriver is off, please turn it on by 'msg=!start'"}
                return jsonify(response)
            sql1.create_msg(msg, "!gpt")
            a=2000
            sys_msg="Successful!"
            while "!gpt"==sql1.last_msg()[2]:
                a-=1
                if a<0:
                    sys_msg="TimeOut!"
                    break
                time.sleep(0.01)
            if sys_msg=="Successful!":
                response=sql1.last_msg()[2]
            else:
                response="Webdriver did not respond in 20 seconds, it may be broken."
            response = {'system': sys_msg, 'message': response}
            return json.dumps(response, ensure_ascii=False)
        else:
            return jsonify({"system": "Please enter a message."})
    else:
        # If the API key is invalid, respond with an error message
        return jsonify({"system": "error",'message': 'Invalid API key. Access denied. Send Get request to this url: http://127.0.0.1:80/api?api_key=saitamatechno&msg=hello'}), 401

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)

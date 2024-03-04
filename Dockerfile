## Custom Dockerfile
FROM consol/debian-xfce-vnc
ENV REFRESHED_AT 2022-10-12
ENV VNC_PW=saitamatechno
ENV VNC_RESOLUTION=1280x720
#ENV RESTART_POLICY=Always

# Switch to root user to install additional software
USER 0
# Set the locale
#RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && \
#    locale-gen
#ENV LANG en_US.UTF-8  
#ENV LANGUAGE en_US:en  
#ENV LC_ALL en_US.UTF-8

#Turkish Language
RUN sed -i '/tr_TR.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen
ENV LANG tr_TR.UTF-8  
ENV LANGUAGE en_US:en
ENV LC_ALL tr_TR.UTF-8

COPY gpt_driver.py /headless/gpt/gpt_driver.py
COPY driver_api.py /headless/gpt/driver_api.py
COPY sql1.py /headless/gpt/sql1.py
COPY gpt_messages.db /headless/gpt/gpt_messages.db
COPY webdriver_status.txt /headless/gpt/webdriver_status.txt

RUN apt-get update -y
RUN apt install nano
RUN apt install python3-pip -y
RUN pip install selenium webdriver_manager Flask

ENV API_KEY="saitamatechno"
CMD python3 /headless/gpt/driver_api.py $API_KEY & python3 /headless/gpt/gpt_driver.py

## switch back to default user
#USER 1000
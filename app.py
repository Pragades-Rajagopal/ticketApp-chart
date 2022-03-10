from flask import Flask, render_template, url_for
import pandas as pd
import os

app = Flask(__name__)

@app.route('/graph/prevMonth')
def graphPrevMonth():

    filePath = os.path.join(os.getcwd(), 'data', 'data.csv')
    dataFrame = pd.read_csv(filePath)

    lbl_inc = dataFrame.loc[dataFrame['TICKET_TYPE'] == 'Incident', 'RESOLUTION']
    labels_inc = [rows for rows in lbl_inc]
    val_inc = dataFrame.loc[dataFrame['TICKET_TYPE'] == 'Incident', 'TICKET_COUNT']
    values_inc = [rows for rows in val_inc]

    lbl_sr = dataFrame.loc[dataFrame['TICKET_TYPE'] == 'Service Request', 'RESOLUTION']
    labels_sr = [rows for rows in lbl_sr]
    val_sr = dataFrame.loc[dataFrame['TICKET_TYPE'] == 'Service Request', 'TICKET_COUNT']
    values_sr = [rows for rows in val_sr]

    mon = dataFrame['MONTH'].unique()
    prevMon = mon[0]

    return render_template("index.html", labels_inc=labels_inc, values_inc=values_inc, labels_sr=labels_sr, values_sr=values_sr, prevMon=prevMon)


@app.route('/graph/curMonth')
def graphCurMonth():

    filePath = os.path.join(os.getcwd(), 'data', 'data_cur.csv')
    dataFrame = pd.read_csv(filePath)

    lbl_inc = dataFrame.loc[dataFrame['TICKET_TYPE'] == 'Incident', 'RESOLUTION']
    labels_inc = [rows for rows in lbl_inc]
    val_inc = dataFrame.loc[dataFrame['TICKET_TYPE'] == 'Incident', 'TICKET_COUNT']
    values_inc = [rows for rows in val_inc]

    lbl_sr = dataFrame.loc[dataFrame['TICKET_TYPE'] == 'Service Request', 'RESOLUTION']
    labels_sr = [rows for rows in lbl_sr]
    val_sr = dataFrame.loc[dataFrame['TICKET_TYPE'] == 'Service Request', 'TICKET_COUNT']
    values_sr = [rows for rows in val_sr]

    mon = dataFrame['MONTH'].unique()
    curMon = mon[0]

    return render_template("index_cur.html", labels_inc=labels_inc, values_inc=values_inc, labels_sr=labels_sr, values_sr=values_sr, curMon=curMon)


if __name__ == "__main__":
    app.run(port=9193, debug=True)
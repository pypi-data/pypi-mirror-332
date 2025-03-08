import scipy.optimize as sp
import scipy.stats as st
from typing import List,Callable
import types
import numpy as np
import zipfile
from io import BytesIO
import xml.etree.ElementTree as ET

def fit_curve(func: Callable,x_vals: List[float],y_vals: List[float],startx:float=None,endx:float=None,starty:float=None,endy:float=None,guess:List[float]=None,maxfev:int=10000)->tuple[Callable,List[float],List[float]]:
    if not isinstance(func, (types.FunctionType)): raise Exception("Bad parameter 'func'")  
    if not isinstance(x_vals, (list,np.ndarray)): raise Exception("Bad parameter 'x_vals'")    
    if not isinstance(y_vals, (list,np.ndarray)): raise Exception("Bad parameter 'y_vals'")        
    if not isinstance(startx, (float,int,types.NoneType)): raise Exception("Bad parameter 'startx'")    
    if not isinstance(endx, (float,int,types.NoneType)): raise Exception("Bad parameter 'endx'")    
    if not isinstance(starty, (float,int,types.NoneType)): raise Exception("Bad parameter 'starty'")    
    if not isinstance(endy, (float,int,types.NoneType)): raise Exception("Bad parameter 'endy'")    
    if not isinstance(guess, (list,types.NoneType,np.ndarray)): raise Exception("Bad parameter 'guess'")    
    if not isinstance(maxfev, (int)): raise Exception("Bad parameter 'maxfev'") 
    if (type(startx) != type(endx)): raise Exception("You can only use startx and endx together")
    if (type(starty) != type(endy)): raise Exception("You can only use starty and endy together")
    if (len(x_vals) < 2): raise Exception("'x_vals' too small")
    if (len(x_vals) != len(y_vals)): raise Exception("Size of 'x_vals' does not match size of 'y_vals'")
    ignore_y,ignore_x = True,True
    if startx != None: ignore_x = False
    else :startx = 0
    if starty != None: ignore_y = False
    else :starty = 0
    x_fit,y_fit=[],[]
    for i in range(0,len(x_vals)):
        x = x_vals[i]
        y = y_vals[i]
        if ((ignore_x or (startx <= x <= endx)) and (ignore_y or (starty <= y <= endy))):
            x_fit.append((x-startx))
            y_fit.append((y-starty)) 
    
    if (len(x_fit)<2): raise Exception("wrong bounds")
    if (guess==None): popt,pcov=sp.curve_fit(func,x_fit,y_fit,maxfev=maxfev)
    else: popt,pcov=sp.curve_fit(func,x_fit,y_fit,p0=guess,maxfev=maxfev)
    return (lambda x: (func((np.array(x)-startx),*popt)+starty) if (isinstance(x,(list,np.ndarray))) else (func((x-startx), *popt))+starty),(popt),(pcov)

def get_data(fileloc: str, sep: str=",", comma: str=".", cols:List[str]=[],breaker: str = "\n",skip:int=0) -> List[float]:
    datalines = []
    with open(fileloc, 'r') as file:
        datalines = file.read().split(breaker)
    data = {}
    none_count = 0
    string_count = 0
    i=skip+1
    if cols == []:
        values = datalines[skip].split(sep)
        for j in range(0,len(values)):
            data[str(values[j])] = []
            cols.append(str(values[j]))
    else:
        i -= 1
    while i < len(datalines):
        values = datalines[i].split(sep)
        if len(data) != len(values):
            if len(datalines) == i+1:
                break
            else: 
                print(r"[Physictools] ERROR: Wrong length of headers at Line %i (Ending...)." % (i+1))
                break
        for j in range(0,len(values)):
            if values[j] != "":
                try: 
                    data[cols[j]].append(float(values[j]))
                except:
                    data[cols[j]].append(str(values[j]))
                    string_count += 1
            else:
                data[cols[j]].append(None)
                none_count += 1
        i += 1
    if none_count > 0: print(r"[Physictools] WARNING: Empty Values found, replaced them with Nones and skipped them. (%i)" % none_count)
    if none_count > 0: print(r"[Physictools] WARNING: String Values found, replaced them with Strings. (%i)" % string_count)
    return data

def fit_and_confidence(func_1:Callable, x_vals:list,y_vals:list,confidence: float = .95,startx:float=0,endx:float=None,starty:float=0,endy:float=None,guess:List[float]=None,maxfev:int=10000) -> tuple[Callable,list,list,list]:
    func, popt,pcov = fit_curve(func_1,x_vals,y_vals,startx=startx,endx=endx,starty=starty,endy=endy,maxfev=maxfev,guess=guess)
    if endx == None: endx = max(x_vals)
    if endy == None: endy = max(y_vals)   
    x_fit, y_fit = [],[]
    for i in range(0,len(x_vals)):
        x = x_vals[i]
        y = y_vals[i]
        if (startx <= x <= endx and starty <= y <= endy):
            x_fit.append((x))
            y_fit.append((y))
    x_vals,y_vals = x_fit,y_fit
    if (isinstance(func,(list,np.ndarray))): y_err = (np.array(y_vals)-np.array(func)).std() * np.sqrt(1/len(x_vals) + (x_vals - x_vals.mean())**2 / np.sum((x_vals - x_vals.mean())**2))
    else: y_err = (np.array(y_vals)-func(np.array(x_vals))).std() * np.sqrt(1/len(x_vals) + (x_vals - np.mean(x_vals))**2 / np.sum((x_vals - np.mean(x_vals))**2))
    y_err *= st.t.ppf((1+confidence)/2,len(x_vals)-len(popt))
    return func,x_vals,func(np.array(x_vals))+y_err,func(np.array(x_vals))-y_err,[popt,pcov]
    
def read_labx(filename: str):
    none_error = False
    with open(filename,"rb") as f: s = f.read()
    with zipfile.ZipFile(BytesIO(s)) as zip_file:
            if "data.xml" in zip_file.namelist():
                with zip_file.open("data.xml") as xml_file:
                    xml= xml_file.read().decode('utf-8')
            else:
                raise ImportError("Broken labx file")
    root = ET.fromstring(xml)
    channels = root[3]
    count = channels.attrib["count"]
    rt = {}
    for i in range(0,int(count)):
        x = channels[i]
        if (int(x[0][4].attrib["count"]) > 0):
            name = x[0][1].text
            arr = []
            for j in range(0,int(x[0][4].attrib["count"])):
                if (x[0][4][j].text) == None:
                    arr.append(None)
                    none_error = True
                else:
                    arr.append(float(x[0][4][j].text))
        rt[name]=arr
    if none_error: print("[Physictools] WARNING: Empty Values found, replaced them with Nones and skipped them.")
    return rt

def lin_regr(x:List,y:List, origin:bool=False,t:float=2.0):    
    x = np.array(x)
    y = np.array(y)
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x2 = np.sum(x**2)
    sum_xy = np.sum(x * y)

    if origin:
        # Berechnung der Koeffizienten
        a = (sum_xy) / (sum_x2)
        b = 0

        # Berechnung von s_y (Standardabweichung der Residuen)
        y_pred = a * x
        sy = np.sqrt(np.sum((y - y_pred) ** 2) / (n - 1))
        # Berechnung der Unsicherheiten von a und b
        sa = sy * np.sqrt(1 / (sum_x2))*t
        sb = 0

    else:
        # Berechnung der Koeffizienten
        a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
        b = (sum_x2 * sum_y - sum_xy * sum_x) / (n * sum_x2 - sum_x**2)

        # Berechnung von s_y (Standardabweichung der Residuen)
        y_pred = a * x + b
        sy = np.sqrt(np.sum((y - y_pred) ** 2) / (n - 2))
        # Berechnung der Unsicherheiten von a und b
        sa = sy * np.sqrt(n / (n * sum_x2 - sum_x**2))*t
        sb = sy * np.sqrt(sum_x2 / (n * sum_x2 - sum_x**2))*t
    return [a,b,sa,sb]


def author():
    print("Thank you for downloading physictools ~ Pulok00")

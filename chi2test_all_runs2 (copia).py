import ROOT as R
import argparse
import errno    
import os

def mkdir_p(path):
    #print "Making dir: ", path
    try:
        os.makedirs(path)
    except OSError as exc:  
        #print("OS error: {0}".format(exc))
        if exc.errno != errno.EEXIST:
          raise
        pass   
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        #possibly handle other errno cases here, otherwise finally:
        else:
            raise Exception('Unknown exception')


def drawHist(h,opath):
    c1 = R.TCanvas()
    c1.SetTickx()
    c1.SetTicky()
    c1.SetLeftMargin(0.1)
    c1.SetRightMargin(0.18)
    
    if h.IsA().InheritsFrom("TEfficiency") == True:
        h.SetFillColor(R.kRed)
        h.Draw("AP")
        c1.Print(opath+"/"+h.GetName()+".png")
    else:
        h.Draw("AP")
        hist_name = opath+h.GetName()+".png"
        c1.Print(opath+"/"+h.GetName()+".png")   
    c1.Update()
    c1.Clear()
    return

def overplot(h1,h2,spec1,spec2,opath,n):
    c1 = R.TCanvas()
    c1.SetTickx()
    c1.SetTicky()
    c1.SetLeftMargin(0.1)
    c1.SetRightMargin(0.18)
    if h1.IsA().InheritsFrom("TEfficiency") == True and h2.IsA().InheritsFrom("TEfficiency") == True:
        h1.SetMarkerStyle(25)
        h2.SetMarkerStyle(25)
        h1.SetMarkerColorAlpha(R.kRed,0.8)
        h2.SetMarkerColorAlpha(R.kBlue,0.8)
        h1.SetLineColor(R.kRed)
        h2.SetLineColor(R.kBlue)
        h22=h2.GetCopyPassedHisto()
        h222=h2.GetCopyTotalHisto()
        h22.Divide(h222)
        
        # Chi-square test

        h11=h1.GetCopyPassedHisto()
        h111=h1.GetCopyTotalHisto()
        h11.Divide(h111)
        #chi21=h22.Chi2Test(h11, "CHI2/NDF P")
        chi21p=h22.Chi2Test(h11, "UU")

        # Print chi-square value

        #chainname = h1.GetName()
        file = open('chi_square_TEff_output.txt',"w")
        #file.write('the name of the chain: {chainname}\n')
        file.write(h1.GetName()+'\n')
        file.write('the TEff value of chi-square: '+chi21p+'\n')
        #file.close()
        
        latex=R.TLatex()
        latex.SetTextSize(0.03)
        latex2=R.TLatex()
        latex2.SetTextSize(0.04)
        latex3=R.TLatex()
        latex3.SetTextSize(0.04)
        #latex4=R.TLatex()
        latex5=R.TLatex()
        latex5.SetTextSize(0.03)
        
        if h1.GetName()=="EffHLT_tauPt_wrt_Offline":
            c1.DrawFrame(0,0,350,1.6)
            latex.DrawLatex(40,1.20,"#chi^{2}="+str(round(chi21p,7)))
            latex2.DrawLatex(25,1.45,"ATLAS internal")
            latex3.DrawLatex(27,1.35,"#sqrt{s}=13.6[TeV]")
            #latex4.DrawLatex(0,1.7,"HLT_tau35_mediumRNN_tracktwoMVA_L1TAU20IM")
            latex5.DrawLatex(300,-0.12, "Pt  [GeV]")
            print(chi21p)
            print("this is the tau pt value of chi21p: ", chi21p)
        elif h1.GetName()=="EffHLT_averageMu_wrt_Offline":
            c1.DrawFrame(0,0.2,65,1.4)
            latex.DrawLatex(7,1.10,"#chi^{2}="+str(round(chi21,7)))
            latex2.DrawLatex(5,1.3,"ATLAS internal")
            latex3.DrawLatex(5,1.20,"#sqrt{s}=13.6[TeV]")
            #latex4.DrawLatex(0,1.45,"HLT_tau35_mediumRNN_tracktwoMVA_L1TAU20IM")
            latex5.DrawLatex(60,0.1, "#mu ")
            print(chi21p)
            print("this is the tau Mu value of chi21p: ", chi21p)
        elif h1.GetName()=="EffHLT_tauEta_wrt_Offline":
            c1.DrawFrame(-3.5,0.65,3.5,1.25)
            latex.DrawLatex(-2.8,1.12,"#chi^{2}="+str(round(chi21,7)))
            latex2.DrawLatex(-3,1.2,"ATLAS internal")
            latex3.DrawLatex(-2.8,1.16,"#sqrt{s}=13.6[TeV]")
            #latex4.DrawLatex(-3.62,1.27,"HLT_tau35_mediumRNN_tracktwoMVA_L1TAU20IM")
            latex5.DrawLatex(3,0.60, "#eta ")
            print(chi21p)
            print("this is the tau eta value of chi21p: ", chi21p)
        elif h1.GetName()=="EffHLT_tauPhi_wrt_Offline":
            c1.DrawFrame(-3.5,0.72,3.5,1.25)
            latex.DrawLatex(-2.65,1.12,"#chi^{2}="+str(round(chi21,7)))
            latex2.DrawLatex(-3,1.2,"ATLAS internal")
            latex3.DrawLatex(-2.8,1.16,"#sqrt{s}=13.6[TeV]")
            #latex4.DrawLatex(-3.62,1.27,"HLT_tau35_mediumRNN_tracktwoMVA_L1TAU20IM")
            latex5.DrawLatex(3,0.67, "#phi")
            print(chi21p)
            print("this is the tau phi value of chi21p: ", chi21p)
        elif h1.GetName()=="EffHLT_tauPt_coarse_wrt_Offline":
            c1.DrawFrame(0,0,350,1.6)
            latex.DrawLatex(40,1.20,"#chi^{2}="+str(round(chi21,7)))
            latex2.DrawLatex(25,1.45,"ATLAS internal")
            latex3.DrawLatex(27,1.35,"#sqrt{s}=13.6[TeV]")
            #latex4.DrawLatex(0,1.7,"HLT_tau35_mediumRNN_tracktwoMVA_L1TAU20IM")
            latex5.DrawLatex(300,-0.12, "Pt  [GeV]")
            print(chi21p)
            print("this is the tau pt coarse value of chi21p: ", chi21p)
        h1.Draw("SAME1")
        h2.Draw("SAME1")
        if h1.GetName()=="EffHLT_tauPt_wrt_Offline":
            h3=R.TLine(n,0,n,1.1)
            h3.SetLineColor(R.kRed)
            h3.Draw("SAME1")
        legend=R.TLegend(0.38,0.7,0.8,0.85)
        legend.AddEntry(h1,spec1,"LEP")
        legend.AddEntry(h2,spec2,"LEP")
        legend.SetBorderSize(0)
        legend.Draw()
        c1.Print(opath+"/"+h1.GetName()+".png")
    elif h1.InheritsFrom("TH1")==True and h2.InheritsFrom("TH1")==True:
        h1.SetMarkerStyle(25)
        h2.SetMarkerStyle(25)
        h1.SetMarkerColorAlpha(R.kRed,0.8)
        h2.SetMarkerColorAlpha(R.kBlue,0.8)
        h1.SetLineColor(R.kRed)
        h2.SetLineColor(R.kBlue)
        

        #chi21=h22.Chi2Test(h11, "CHI2/NDF P")
        chi21th1p=h2.Chi2Test(h1, "UU")

        if h1.GetMaximumBin()>h2.GetMaximumBin():
            h1.Draw("SAME1")
            h2.Draw("SAME1")
        else:
            h2.Draw("SAME1")
            h1.Draw("SAME1")
        print("chi21p is: ",chi21th1p)
        
        # Retrieve the chisquare test

        file2 = open('chi_square_TH1_output.txt',"w")
        file2.write(h1.GetName()+'\n')
        file2.write('the TH1 value of chi-square:'+chi21p+'\n')
        #file2.close()

        legend=R.TLegend(0.6,0.9,1,1)
        legend.AddEntry(h1,spec1,"L")
        legend.AddEntry(h2,spec2,"L")
        legend.Draw()
        c1.Print(opath+"/"+h1.GetName()+".png")
        
    c1.Update()
    c1.Clear()
    return


def loopDir(obj,opath=""):
    if obj.IsA().InheritsFrom("TDirectoryFile") == True:
        opath += "/"+obj.GetName()
        mkdir_p(opath)
        for keys in obj.GetListOfKeys():
           obj2 = keys.ReadObj()
           if obj2.IsA().InheritsFrom("TEfficiency") == True:
              drawHist(obj2,opath)
           elif obj2.IsA().InheritsFrom("TDirectoryFile") == True:
              loopDir(obj2,opath)
    else: 
        return
    
def loop2Dir(hist1,hist2,spec1,spec2,n,opath=""):
    if hist1.IsA().InheritsFrom("TDirectoryFile") == True:
        opath = opath +"/"+hist2.GetName()
        mkdir_p(opath)
        a=0
        dic={}
        for key in hist2.GetListOfKeys():
            dic[key.GetName()]=key
        for keys in hist1.GetListOfKeys():
            name=keys.GetName()
            for keyss in hist2.GetListOfKeys():
                if keyss.GetName()==name:
                    obj1 = keys.ReadObj()
                    obj2=dic[name].ReadObj()
                    if obj1.IsA().InheritsFrom("TEfficiency")==True or obj1.IsA().InheritsFrom("TH1")==True:
                        overplot(obj1,obj2,spec1,spec2,opath,n)
                    elif obj1.IsA().InheritsFrom("TDirectoryFile")==True:
                        loop2Dir(obj1,obj2,spec1,spec2,n,opath)
                  
            a+=1
        print(opath)
    else: 
        return
def GetStream(file=""):
    a=""
    path="_"
    for letter in file:
        a+=letter
        if a[-7:-1]=="data22":
            path=a[:-7]
            a=""
        elif a==path:
            a=""
        elif a[-13:-1]=="physics_Main":
            stream="Physics_Main"
        elif a[-16:-1]=="express_express":
            stream="Express_Express"
    return stream
    
def GetRunNumber(file=""):
    a=""
    run="_"
    path="_"
    for letter in file:
        a+=letter
        if a[-7:-1]=="data22":
            path=a[:-7]
    a=""
    for letter in file:
        a+=letter
        if a==path:
            a=""
        elif a[0:17]=="data22_13p6TeV.00" and run[-1]!=".":
            run+=letter
    return run[2:8]

def GetTag(file=""):
    a=""
    n1=-6
    n2=-1
    tag="_"
    path="_"
    for letter in file:
        a+=letter
        if a[-7:-1]=="data22":
            path=a[:-7]
            a=""
        elif a==path:
            a=""
        elif a[n1:n2]=="HIST." and tag[-1]!=".":
            tag+=letter
            n1-=1
            n2-=1
    return tag[:-1]
def getn(path=""):
    a=""
    n=0
    for l in path:
        a+=l
        if a[-11:-4]=="HLT_tau":
            if a[-3]=="_":
                n=a[-4:-3]
            elif a[-2]=="_":
                n=a[-4:-2]
            else:
                n=a[-4:-1]
    return int(n)
R.gROOT.SetBatch(True)
path_run="main/source/path/with/a/lot/of/subfolder/"
file1=input("Reference path:")
#/cloud/reference/path/HIST.30220625._000001.pool.root.1
for run in os.listdir(path_run):
    for fold in os.listdir(path_run+"/"+run):
        if "Main.merge.HIST" in str(fold) and len(os.listdir(path_run+"/"+run+"/"+fold))>0:
            file2=path_run+"/"+run+"/"+fold+"/"+os.listdir(path_run+"/"+run+"/"+fold)[0]
            if not os.path.exists("plots2/Overlayed/"+GetStream(file1) +"_Run"+ GetRunNumber(file1)+"+"+ GetStream(file2) +"_Run"+ GetRunNumber(file2)):
                specific="Run"+GetRunNumber(file1)+"Hist"+GetTag(file1)
                specific2="Run"+GetRunNumber(file2)+"Hist"+GetTag(file2)
    
                output_path = "plots2/" + GetStream(file1) +"_"+ GetRunNumber(file1) + GetTag(file1)
                if not os.path.exists(output_path):
                    print("Creating output directory: ", output_path)
                    mkdir_p(output_path)
                output_path2 = "plots2/" + GetStream(file2) +"_"+ GetRunNumber(file2) + GetTag(file2)
                if not os.path.exists(output_path2):
                    print("Creating output directory: ", output_path2)
                    mkdir_p(output_path2)
                output_path_op = "plots2/Overlayed/" + GetStream(file1) +"_Run"+ GetRunNumber(file1)+"+"+ GetStream(file2) +"_Run"+ GetRunNumber(file2)
                if not os.path.exists(output_path_op):
                    print("Creating output directory: ", output_path_op)
                    mkdir_p(output_path_op) 

                ROOT_file_base_dir = "run_" + GetRunNumber(file1) + "/HLT/TauMon"
                ROOT_file_base_dir2 = "run_" + GetRunNumber(file2) + "/HLT/TauMon"
    
                ROOT_file = R.TFile.Open(file1, "read")
                ROOT_file2 = R.TFile.Open(file2, "read")

                get_keys_base_dir = ROOT_file.Get(ROOT_file_base_dir)
                get_keys_base_dir2 = ROOT_file2.Get(ROOT_file_base_dir2)

                print("Base ROOT dir in the files is: ", ROOT_file_base_dir)
                print("Base ROOT dir 2 in the files is: ", ROOT_file_base_dir2)

                dic={}
                dic2={}
                lista=[]
                print("IsA is ",get_keys_base_dir2.IsA())
                if get_keys_base_dir2.IsA().InheritsFrom("TDirectoryFile")==True:
                    for keysROOTFile in get_keys_base_dir.GetListOfKeys():
                        get_keys_dir = keysROOTFile.GetName()
                        get_type = keysROOTFile.GetClassName()
                        print(get_keys_dir," ",get_type)
                        lista.append(keysROOTFile.ReadObj())
                        dic[get_keys_dir]=keysROOTFile.ReadObj()
                        obj = keysROOTFile.ReadObj()
                        loopDir(obj,output_path)
                    a=0    
                    for keysROOTFile2 in get_keys_base_dir2.GetListOfKeys():
                        get_keys_dir2 = keysROOTFile2.GetName()
                        get_type2 = keysROOTFile2.GetClassName()
                        print(get_keys_dir2," ",get_type2)
                        dic2[get_keys_dir2]=keysROOTFile2.ReadObj()
                        obj2 = keysROOTFile2.ReadObj()
                        obj1=get_keys_base_dir.GetListOfKeys()[a].ReadObj()
                        n=getn(obj2.GetName())
                        print(n)
                        loopDir(obj2,output_path2)
                        loop2Dir(obj1,obj2,specific,specific2,n,output_path_op)
                        a+=1

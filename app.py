import streamlit as st

# Application Title
st.title("Company Code Tracker")

# Initial Data List
codesdone = '''MXI EQX AYS zzz CCV PRT TGA PGC TWR NZM MHI PGR MSG UBI IGN AAU RDG
  ASV WLD zzz MRM HIL CL1 MOZ WPP SIG API TNK GOW WCG ERL SWM SHM LPE CYC zzz A2B
  FOD AKG TRS HIT SIT MYR NTD KRM SIQ HNG GGE KPG CLB ISU SGF EP1 MOC GTN MSL zzz CLX
  zzz HZN TAP MHJ SRV LCM 8CO GO2 SIO EDU ISD BOL AMO VOR ERA BKY CIW AD8 FIJ TEG ZLD
  SNL DDT AHF BEE KAM OLI TBR A2M SM1 VOL APX MCP HYD TZL GDA AGL SSM YFZ LAU zzz zzz
  MWY AU1 EM1 zzz zzz EZZ MMJ WSI VVA zzz LSH RVR SBW AL8 SWF GMA GNP MEA VBC TPC QHL BGD POW zzz AMP
  MDR CNW ADH DTC COS PTM STP TTI IDT MCL SIV MFG PTL LVT ABY RZI KGN WGN BKG VGI
  SUL SSG DSK CUP BPT PDL PNV DCG BMT NAM FRM MKL OSP UOS CXZ HPG SXL TRT E33 PPL
  zzz 3DP CUV CBO MME AVG AX1 zzz CDA FLC zzz NCK TIP ANN 29M PSQ WZR TUA CLT zzz
  RBR GUL TCO XF1 CLA OXT XTE PXS ODA WSP VMC NOL RBL CTT MGH CCX NWC TRJ TPW EQS EML
  AHX ATH ARC DDB NHC MAY GLB ILA HMI FID PPE BBN MXO BWF MP1 POS STO ACR HVN GDC zzz zzz zzz zzz
FYI DXB MTO EOS ABB ALC FCL RLG VIT RIE CMP GBZ JDO TLM KME XRF PRO ABA UNI FDV CAI
LOV CHL BUB MGL VHT CYG LGP VQA SRX YBR IGL A1N RKN RMC RPM HPP HGV SRH PLT ALK SHE
CLG AHC RFT SEQ HAL DCL CLW RUL BRI IFL SEN ALD PPK CVV DUR AWC FPC ARX CL8 WNX GLE
CGO ACU EMB SKS NOU VRS MFD PFG PNC ASH CAF IRI DVR EAX MLG GRR DRO KYP EXP NIC APL
MLX HCF KMD BRK AVC CLV WTL MPR RXH REX BLX SXE TEA LRK HGO IEL PWR APE WOSG EVO FWD
THL WRKR PTLO GEM EGG SLH WJL TRP DMP RFG BRBY DOL PIL LULU RBR SOC GNG DUR HLO SND
BSA BRL MCE GRR AER NEC WISE GATC IMB DDR ETSY MDP OLH VEA WEB AAR OEL MAM SYL PKD
AAL COG FMG DNP JLG AAT PTN MIN CCG GTN SSP WIN G88 RYM CX PHX XRO EDGM CVN OSCR LBL
TGA.L AAP SKO GOOGL RHI BTI BWN CZR 1CG WU CYL KAR 5GN SSH TW.L EVO RHT KPO WINE'''

# Process the data
cdl = codesdone.split()
total_companies = len(cdl) - cdl.count('zzz')

# Sidebar Dashboard Metrics
st.sidebar.header("Dashboard Metrics")
st.sidebar.metric(label="Total Unique Companies Done", value=total_companies)

# Duplicate Check Error Display
duplicates = []
for i in range(len(cdl)):
    if cdl.count(cdl[i]) > 1 and cdl[i] != 'zzz':
        duplicates.append(f"**{cdl[i]}** at position {i}")

if duplicates:
    st.sidebar.error("🚨 Duplicate entries found:")
    for dup in set(duplicates):
        st.sidebar.write(dup)

# Main Application Logic
st.subheader("Search Company Codes")
code = st.text_input("Enter a code to check:", max_chars=10).upper().strip()

if code:
    if code in cdl:
        st.success(f"✅ **{code}** has been done.")
        
        # Calculate precise indexing
        code_number = cdl.index(code)
        adjusted_index = code_number + 1 - cdl[0:code_number].count('zzz')
        
        # Display list metrics
        st.write(f"📌 Code **{code}** is number **{adjusted_index}** in the list of **{total_companies}** active companies.")
        
        # Surrounding context strings
        before_context = cdl[max(0, code_number-3):code_number]
        after_context = cdl[code_number+1:code_number+4]
        st.info(f"🔍 Context: Appears after `{before_context}` and before `{after_context}`")
        
        # Delphiforums Link Redirection Button
        target_url = f"https://forums.delphiforums.com/fund/messages/?msg=19.{code_number + 1}"
        st.link_button("🌐 Open Forum Analysis", target_url, use_container_width=True)

    else:
        st.warning(f"❌ **{code}** has NOT been done.")

# Expandable Master List View
st.markdown("---")
with st.expander("📋 View Complete Master Code List"):
    st.code(codesdone, language="text")

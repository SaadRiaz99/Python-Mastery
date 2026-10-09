import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def create_assignment():
    doc = Document()

    # ---------------------------------------------------------
    # Page Setup (Margins)
    # ---------------------------------------------------------
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)

    # Base Colors
    NAVY = RGBColor(0, 51, 102)        # #003366
    SLATE = RGBColor(74, 96, 122)      # #4A607A
    DARK_TEXT = RGBColor(34, 34, 34)   # #222222
    CODE_COLOR = RGBColor(40, 40, 40)  # #282828
    WHITE = RGBColor(255, 255, 255)

    HEX_NAVY = "003366"
    HEX_SLATE = "4A607A"
    HEX_LIGHT_BG = "F4F6F9"
    HEX_ALT_ROW = "F9FBFD"
    HEX_BORDER = "CCCCCC"

    # Helper Functions
    def set_cell_background(cell, fill_hex):
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
        cell._tc.get_or_add_tcPr().append(shd)

    def set_cell_margins(cell, top=120, bottom=120, left=180, right=180):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)

    def set_table_borders(table, color="D3D3D3", sz="4", val="single"):
        tblPr = table._tbl.tblPr
        borders = parse_xml(f'<w:tblBorders {nsdecls("w")}><w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/><w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/><w:left w:val="none"/><w:right w:val="none"/><w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/><w:insideV w:val="none"/></w:tblBorders>')
        tblPr.append(borders)

    def add_heading_1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(8)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(18)
        run.font.bold = True
        run.font.color.rgb = NAVY
        return p

    def add_heading_2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(14)
        run.font.bold = True
        run.font.color.rgb = SLATE
        return p

    def add_heading_3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = DARK_TEXT
        return p

    def add_body(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.font.name = 'Calibri'
            r_bold.font.size = Pt(11)
            r_bold.font.bold = True
            r_bold.font.color.rgb = DARK_TEXT
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(11)
        run.font.color.rgb = DARK_TEXT
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_bold = p.add_run(bold_prefix)
            r_bold.font.name = 'Calibri'
            r_bold.font.size = Pt(11)
            r_bold.font.bold = True
            r_bold.font.color.rgb = DARK_TEXT
        run = p.add_run(text)
        run.font.name = 'Calibri'
        run.font.size = Pt(11)
        run.font.color.rgb = DARK_TEXT
        return p

    def add_code_block(code_text):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = table.cell(0, 0)
        cell.width = Inches(6.5)
        set_cell_background(cell, HEX_LIGHT_BG)
        set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
        
        # Add border
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(f'<w:tcBorders {nsdecls("w")}><w:top w:val="single" w:sz="6" w:space="0" w:color="{HEX_SLATE}"/><w:left w:val="single" w:sz="18" w:space="0" w:color="{HEX_NAVY}"/><w:bottom w:val="single" w:sz="6" w:space="0" w:color="{HEX_SLATE}"/><w:right w:val="single" w:sz="6" w:space="0" w:color="{HEX_SLATE}"/></w:tcBorders>')
        tcPr.append(borders)

        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.15

        lines = code_text.strip().split('\n')
        for i, line in enumerate(lines):
            if i > 0:
                p = cell.add_paragraph()
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(0)
                p.paragraph_format.line_spacing = 1.15
            run = p.add_run(line)
            run.font.name = 'Consolas'
            run.font.size = Pt(9.5)
            run.font.color.rgb = CODE_COLOR

        doc.add_paragraph().paragraph_format.space_after = Pt(6)

    def add_image_with_caption(img_path, caption_text, width=Inches(5.8)):
        if os.path.exists(img_path):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            
            run = p.add_run()
            run.add_picture(img_path, width=width)

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(2)
            p_cap.paragraph_format.space_after = Pt(12)
            
            r_cap = p_cap.add_run(caption_text)
            r_cap.font.name = 'Calibri'
            r_cap.font.size = Pt(9.5)
            r_cap.font.italic = True
            r_cap.font.color.rgb = SLATE

    # =========================================================
    # COVER PAGE
    # =========================================================
    cover_p_space = doc.add_paragraph()
    cover_p_space.paragraph_format.space_before = Pt(30)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_after = Pt(6)
    r_title = p_title.add_run("COMPUTER NETWORKS")
    r_title.font.name = 'Calibri'
    r_title.font.size = Pt(26)
    r_title.font.bold = True
    r_title.font.color.rgb = NAVY

    # Subtitle
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(24)
    r_sub = p_sub.add_run("LAB ASSIGNMENT 01\nIPv6 Subnetting & Basic Switch Configuration")
    r_sub.font.name = 'Calibri'
    r_sub.font.size = Pt(18)
    r_sub.font.bold = True
    r_sub.font.color.rgb = SLATE

    # Divider Line
    p_div = doc.add_paragraph()
    p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_div.paragraph_format.space_after = Pt(40)
    r_div = p_div.add_run("―" * 35)
    r_div.font.color.rgb = SLATE

    # Group Members Header
    p_gm = doc.add_paragraph()
    p_gm.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_gm.paragraph_format.space_after = Pt(12)
    r_gm = p_gm.add_run("Submitted By (Group Members):")
    r_gm.font.name = 'Calibri'
    r_gm.font.size = Pt(13)
    r_gm.font.bold = True
    r_gm.font.color.rgb = NAVY

    # Members Table / Centered text box
    members = [
        "Saad Bin Riaz  (BAI-25F-035)",
        "Umair Hayat  (BAI-25F-033)",
        "Ayesha Zahid  (BAI-25F-026)",
        "Laiba Ameer  (BAI-25F-001)"
    ]
    for m in members:
        p_m = doc.add_paragraph()
        p_m.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_m.paragraph_format.space_after = Pt(4)
        r_m = p_m.add_run(m)
        r_m.font.name = 'Calibri'
        r_m.font.size = Pt(14)
        r_m.font.bold = True
        r_m.font.color.rgb = DARK_TEXT

    p_space2 = doc.add_paragraph()
    p_space2.paragraph_format.space_before = Pt(50)

    # Department & Date Info
    p_info = doc.add_paragraph()
    p_info.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_info.paragraph_format.space_after = Pt(4)
    r_info = p_info.add_run("Department of Computer Science & Information Technology")
    r_info.font.name = 'Calibri'
    r_info.font.size = Pt(11)
    r_info.font.italic = True
    r_info.font.color.rgb = SLATE

    p_date = doc.add_paragraph()
    p_date.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_date.paragraph_format.space_after = Pt(0)
    r_date = p_date.add_run("October 2026")
    r_date.font.name = 'Calibri'
    r_date.font.size = Pt(11)
    r_date.font.color.rgb = SLATE

    doc.add_page_break()

    # Enable Header/Footer for subsequent pages
    main_section = doc.sections[0]
    header = main_section.header
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("Computer Networks | Assignment 01: IPv6 Subnetting & Switch Configuration")
    hrun.font.name = 'Calibri'
    hrun.font.size = Pt(8.5)
    hrun.font.color.rgb = SLATE

    # =========================================================
    # SECTION 1: IPv6 SUBNETTING & MATHEMATICAL CALCULATIONS
    # =========================================================
    add_heading_1("1. IPv6 Subnetting & Mathematical Calculations")
    
    add_body("This section details the step-by-step mathematical derivation for subnetting the assigned IPv6 network block. The primary goal is to allocate smaller, equal-sized subnets (pools) with a specific host capacity per pool from the original prefix.")
    
    add_heading_2("1.1 Network Requirements & Given Data")
    add_bullet(" 2001:DB8:1234:5678::/120", "Original IPv6 Network Prefix:")
    add_bullet(" 120 bits", "Original Prefix Length:")
    add_bullet(" 16 addresses per subnet pool", "Required Host Addresses per Pool:")

    add_heading_2("1.2 Step-by-Step Subnetting Derivation")

    add_heading_3("Step 1: Calculate Required Host Bits (n)")
    add_body("To determine the number of host bits (n) required to accommodate 16 IP addresses in each pool, we use the standard exponential formula:")
    add_code_block("2^n = Required Host Addresses\n2^n = 16\n2^4 = 16  ==>  n = 4 host bits")
    add_body("Thus, exactly 4 host bits are reserved for host addressing within each pool.")

    add_heading_3("Step 2: Calculate New Subnet Prefix Length")
    add_body("An IPv6 address consists of 128 total bits. Subtracting the host bits (n = 4) from 128 gives the new prefix length:")
    add_code_block("New Prefix Length = Total IPv6 Bits - Host Bits\nNew Prefix Length = 128 - 4 = /124\nOld Prefix = /120  -->  New Subnet Prefix = /124")

    add_heading_3("Step 3: Calculate Subnet Bits & Total Available Pools")
    add_body("The number of bits borrowed for subnetting is calculated by finding the difference between the new prefix length and the old prefix length:")
    add_code_block("Subnet Bits = New Prefix Length - Old Prefix Length\nSubnet Bits = 124 - 120 = 4 bits\n\nTotal Subnet Pools = 2^(Subnet Bits) = 2^4 = 16 Subnet Pools")
    add_body("The network is divided into 16 distinct subnet pools.")

    add_heading_3("Step 4: Determine Block Size & Hexadecimal Jump")
    add_body("The block size represents the number of total IP addresses contained in each subnet pool:")
    add_code_block("Block Size (Decimal) = 2^(128 - 124) = 2^4 = 16 Addresses per Pool\n16 (Decimal) = 10 (Hexadecimal)  [Since 16_10 = 10_16]")
    add_body("Because IPv6 addresses are written in hexadecimal format, the subnet boundary increments (jumps) by 0x10 in the lowest hex digit of the prefix:")
    add_code_block("Hexadecimal Jump Sequence:\n00 -> 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80 -> 90 -> A0 -> B0 -> C0 -> D0 -> E0 -> F0")

    add_heading_2("1.3 Complete IPv6 Subnet Pools Table")
    add_body("The table below presents all 16 generated IPv6 pools along with their subnet prefix and usable address ranges:")

    # Table of Pools
    table_pools = doc.add_table(rows=17, cols=3)
    table_pools.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_pools)

    headers = ["Pool #", "Subnet Prefix (/124)", "Usable Address Range"]
    col_widths = [Inches(1.0), Inches(2.7), Inches(2.8)]

    # Style Header Row
    hdr_cells = table_pools.rows[0].cells
    for i, title in enumerate(headers):
        hdr_cells[i].width = col_widths[i]
        set_cell_background(hdr_cells[i], HEX_NAVY)
        set_cell_margins(hdr_cells[i], top=100, bottom=100, left=150, right=150)
        p = hdr_cells[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(title)
        r.font.name = 'Calibri'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = WHITE

    pools_data = [
        ("Pool 1", "2001:DB8:1234:5678::00/124", "2001:DB8:1234:5678::00 - ::0F"),
        ("Pool 2", "2001:DB8:1234:5678::10/124", "2001:DB8:1234:5678::10 - ::1F"),
        ("Pool 3", "2001:DB8:1234:5678::20/124", "2001:DB8:1234:5678::20 - ::2F"),
        ("Pool 4", "2001:DB8:1234:5678::30/124", "2001:DB8:1234:5678::30 - ::3F"),
        ("Pool 5", "2001:DB8:1234:5678::40/124", "2001:DB8:1234:5678::40 - ::4F"),
        ("Pool 6", "2001:DB8:1234:5678::50/124", "2001:DB8:1234:5678::50 - ::5F"),
        ("Pool 7", "2001:DB8:1234:5678::60/124", "2001:DB8:1234:5678::60 - ::6F"),
        ("Pool 8", "2001:DB8:1234:5678::70/124", "2001:DB8:1234:5678::70 - ::7F"),
        ("Pool 9", "2001:DB8:1234:5678::80/124", "2001:DB8:1234:5678::80 - ::8F"),
        ("Pool 10", "2001:DB8:1234:5678::90/124", "2001:DB8:1234:5678::90 - ::9F"),
        ("Pool 11", "2001:DB8:1234:5678::A0/124", "2001:DB8:1234:5678::A0 - ::AF"),
        ("Pool 12", "2001:DB8:1234:5678::B0/124", "2001:DB8:1234:5678::B0 - ::BF"),
        ("Pool 13", "2001:DB8:1234:5678::C0/124", "2001:DB8:1234:5678::C0 - ::CF"),
        ("Pool 14", "2001:DB8:1234:5678::D0/124", "2001:DB8:1234:5678::D0 - ::DF"),
        ("Pool 15", "2001:DB8:1234:5678::E0/124", "2001:DB8:1234:5678::E0 - ::EF"),
        ("Pool 16", "2001:DB8:1234:5678::F0/124", "2001:DB8:1234:5678::F0 - ::FF"),
    ]

    for idx, (p_num, p_pref, p_range) in enumerate(pools_data):
        row_cells = table_pools.rows[idx + 1].cells
        bg_color = HEX_ALT_ROW if idx % 2 == 1 else "FFFFFF"
        for i, val in enumerate([p_num, p_pref, p_range]):
            row_cells[i].width = col_widths[i]
            set_cell_background(row_cells[i], bg_color)
            set_cell_margins(row_cells[i], top=80, bottom=80, left=120, right=120)
            p = row_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i == 0 else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = 'Consolas' if i > 0 else 'Calibri'
            r.font.size = Pt(9.5 if i > 0 else 10)
            r.font.color.rgb = DARK_TEXT

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    add_heading_2("1.4 Verification with Solution Worksheets")
    add_body("The handwritten calculation worksheets recorded during the assignment preparation are shown below for complete documentation and verification:")

    add_image_with_caption("1.jpeg", "Figure 1.1: Handwritten Subnetting Derivation (Host bits, new prefix length, and total pools calculation)", width=Inches(4.8))
    add_image_with_caption("2.jpeg", "Figure 1.2: Handwritten Pool List & Decimal to Hexadecimal Conversion (16_10 = 10_16)", width=Inches(4.8))
    add_image_with_caption("3.jpeg", "Figure 1.3: Handwritten Summary Sheet (Original network, new prefix, block size, and hexadecimal jump pattern)", width=Inches(4.8))

    # =========================================================
    # SECTION 2: CISCO PACKET TRACER TOPOLOGY SETUP
    # =========================================================
    add_heading_1("2. Cisco Packet Tracer Network Topology & IP Configuration")
    
    add_body("The calculated IPv6 subnets were deployed in Cisco Packet Tracer to construct a functional multi-switch network infrastructure. Pool 2 (2001:DB8:1234:5678::10/124) was selected for host IP assignment across the network.")

    add_heading_2("2.1 Topology Overview")
    add_bullet(" Two Cisco Catalyst 2960 24-Port FastEthernet Switches (Switch0 and Switch1).", "Switch Devices:")
    add_bullet(" 10 Personal Computers (PC0 to PC9).", "End User Devices:")
    add_bullet(" PC0, PC1, PC2, PC3, PC4 connected via copper straight-through cables.", "Switch0 Cluster:")
    add_bullet(" PC5, PC6, PC7, PC8, PC9 connected via copper straight-through cables.", "Switch1 Cluster:")
    add_bullet(" Direct Ethernet crossover cable linking Switch0 and Switch1 to enable inter-switch communication.", "Inter-Switch Trunk Link:")

    add_image_with_caption("WhatsAp Image 2026-10-05 at 10.00.32 PM.jpeg", "Figure 2.1: Cisco Packet Tracer Network Topology showing Switch0, Switch1, connected PCs, and real-time ICMP PDU status", width=Inches(6.2))

    add_heading_2("2.2 PC IPv6 Addressing Table")
    add_body("All PCs are statically configured using addresses from Subnet Pool 2 (2001:DB8:1234:5678::10/124):")

    table_pcs = doc.add_table(rows=11, cols=4)
    table_pcs.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table_pcs)

    headers_pc = ["Device", "Connected Switch", "IPv6 Address", "Subnet Mask / Prefix"]
    widths_pc = [Inches(1.0), Inches(1.5), Inches(2.7), Inches(1.3)]

    hdr_cells_pc = table_pcs.rows[0].cells
    for i, title in enumerate(headers_pc):
        hdr_cells_pc[i].width = widths_pc[i]
        set_cell_background(hdr_cells_pc[i], HEX_NAVY)
        set_cell_margins(hdr_cells_pc[i], top=100, bottom=100, left=120, right=120)
        p = hdr_cells_pc[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(title)
        r.font.name = 'Calibri'
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = WHITE

    pc_records = [
        ("PC0", "Switch0", "2001:DB8:1234:5678::10", "/124"),
        ("PC1", "Switch0", "2001:DB8:1234:5678::11", "/124"),
        ("PC2", "Switch0", "2001:DB8:1234:5678::12", "/124"),
        ("PC3", "Switch0", "2001:DB8:1234:5678::13", "/124"),
        ("PC4", "Switch0", "2001:DB8:1234:5678::14", "/124"),
        ("PC5", "Switch1", "2001:DB8:1234:5678::15", "/124"),
        ("PC6", "Switch1", "2001:DB8:1234:5678::16", "/124"),
        ("PC7", "Switch1", "2001:DB8:1234:5678::17", "/124"),
        ("PC8", "Switch1", "2001:DB8:1234:5678::18", "/124"),
        ("PC9", "Switch1", "2001:DB8:1234:5678::19", "/124"),
    ]

    for idx, (d_name, d_sw, d_ip, d_pref) in enumerate(pc_records):
        row_cells = table_pcs.rows[idx + 1].cells
        bg_color = HEX_ALT_ROW if idx % 2 == 1 else "FFFFFF"
        for i, val in enumerate([d_name, d_sw, d_ip, d_pref]):
            row_cells[i].width = widths_pc[i]
            set_cell_background(row_cells[i], bg_color)
            set_cell_margins(row_cells[i], top=70, bottom=70, left=100, right=100)
            p = row_cells[i].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [0, 1, 3] else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = 'Consolas' if i == 2 else 'Calibri'
            r.font.size = Pt(9.5 if i == 2 else 10)
            r.font.color.rgb = DARK_TEXT

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    add_heading_2("2.3 Host IP Configuration Proof")
    add_body("Screenshots from Cisco Packet Tracer showing the exact IP configuration interface for PC0 and PC9 are embedded below:")

    add_image_with_caption("WhatsApp Image 2026-10-05 at 101.jpeg", "Figure 2.2: Static IPv6 configuration on PC0 (Address: 2001:DB8:1234:5678::10/124)", width=Inches(5.8))
    add_image_with_caption("WhatsApp Image 2026-10-05 at 10.jpeg", "Figure 2.3: Static IPv6 configuration on PC9 (Address: 2001:DB8:1234:5678::19/124)", width=Inches(5.8))

    # =========================================================
    # SECTION 3: BASIC SWITCH CONFIGURATION & SECURITY
    # =========================================================
    add_heading_1("3. Basic Switch CLI Security & Device Configuration")
    
    add_body("To secure network infrastructure devices, Cisco IOS CLI commands were configured on both Switch0 (SW3) and Switch1 (SW1). These configurations enforce hostname identification, domain lookup suppression, access security, password encryption, and legal warning banners.")

    add_heading_2("3.1 Standard Cisco IOS Security Configuration Script")
    add_body("The complete set of Cisco IOS commands executed on each switch is as follows:")

    cisco_cmd_script = """! Enter Privileged EXEC and Global Configuration Mode
enable
configure terminal

! 1. Assign Device Hostname
hostname SW3  (or SW1 for Switch 1)

! 2. Disable Unnecessary DNS Lookups to Prevent CLI Freezes
no ip domain-lookup

! 3. Configure Message of the Day (MOTD) Legal Banner
banner motd #Authorized Access Only! Unauthorized users will be prosecuted.#

! 4. Set Encrypted Enable Secret Password for Privileged Access
enable secret cisco123

! 5. Secure Console Access Line (Line Con 0)
line console 0
 password cisco
 login
 exit

! 6. Secure Virtual Terminal Lines for Remote Telnet/SSH Access (Lines VTY 0 4)
line vty 0 4
 password cisco
 login
 exit

! 7. Encrypt Plaintext Passwords in Running Configuration
service password-encryption

! 8. Exit Configuration Mode and Save to NVRAM
end
copy running-config startup-config"""

    add_code_block(cisco_cmd_script)

    add_heading_2("3.2 Command Purpose & Security Explanation")
    add_bullet(" Identifies the switch uniquely on the network for administrative clarity.", "hostname <name>:")
    add_bullet(" Prevents the switch from attempting to resolve mistyped commands as domain names, avoiding annoying CLI command hangs.", "no ip domain-lookup:")
    add_bullet(" Displays an official legal notice to any user attempting to access the CLI interface, providing legal protection against unauthorized intrusion.", "banner motd #...#:")
    add_bullet(" Protects access to Privileged EXEC mode using a strong MD5-hashed password (cisco123).", "enable secret cisco123:")
    add_bullet(" Enforces password authentication ('cisco') on physical serial/console port connections.", "line console 0 & login:")
    add_bullet(" Requires password authentication ('cisco') for incoming Telnet and SSH sessions on lines 0 through 4.", "line vty 0 4 & login:")
    add_bullet(" Converts all plain-text passwords stored in the configuration file into Type-7 encrypted strings to prevent shoulder surfing.", "service password-encryption:")
    add_bullet(" Writes active running configurations from RAM to non-volatile RAM (NVRAM) so configurations persist across reboots.", "copy running-config startup-config:")

    add_heading_2("3.3 Switch 0 (SW3) Configuration & Verification")
    add_body("Below is the CLI output showing the complete configuration execution on Switch 0 (SW3), followed by login prompt verification showing the MOTD legal banner and password enforcement:")

    add_image_with_caption("WhatsApp Image 2026.jpeg", "Figure 3.1: Switch 0 CLI terminal output executing hostname, banner, passwords, encryption, and startup-config copy", width=Inches(5.8))
    add_image_with_caption("WhatsApp Image 2026-10-05 a.jpeg", "Figure 3.2: Switch 0 console security verification showing MOTD banner and password prompt upon user connection", width=Inches(5.8))

    add_heading_2("3.4 Switch 1 (SW1) Configuration & Verification")
    add_body("Similarly, Switch 1 (SW1) was configured with identical security standards. Below are the CLI command execution logs and console security verification screenshots:")

    add_image_with_caption("WhatsApp Image 2026-10-05 at 10.00.30 PM.jpeg", "Figure 3.3: Switch 1 CLI terminal output applying hostname SW1, banner motd, enable secret, line passwords, and saving configuration", width=Inches(5.8))
    add_image_with_caption("WhatsApp Image.jpeg", "Figure 3.4: Switch 1 console login prompt demonstrating banner display and password authentication access control", width=Inches(5.8))

    # =========================================================
    # SECTION 4: END-TO-END CONNECTIVITY VERIFICATION
    # =========================================================
    add_heading_1("4. End-to-End Connectivity Verification & Testing")
    
    add_body("To verify proper physical connectivity, correct IPv6 subnet configuration, and layer-2 switch forwarding across the inter-switch trunk cable, an end-to-end ICMP ping test was performed between host PC0 (connected to Switch 0) and host PC9 (connected to Switch 1).")

    add_heading_2("4.1 Ping Test Execution")
    add_body("From host PC0 (IPv6: 2001:DB8:1234:5678::10), the Command Prompt was opened and the ICMPv6 ping command was issued targeting PC9 (IPv6: 2001:DB8:1234:5678::19):")
    
    add_code_block("C:\\> ping 2001:DB8:1234:5678::19\n\nPinging 2001:DB8:1234:5678::19 with 32 bytes of data:\n\nReply from 2001:DB8:1234:5678::19: bytes=32 time<1ms TTL=128\nReply from 2001:DB8:1234:5678::19: bytes=32 time<1ms TTL=128\nReply from 2001:DB8:1234:5678::19: bytes=32 time<1ms TTL=128\nReply from 2001:DB8:1234:5678::19: bytes=32 time<1ms TTL=128\n\nPing statistics for 2001:DB8:1234:5678::19:\n    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),\nApproximate round trip times in milli-seconds:\n    Minimum = 0ms, Maximum = 1ms, Average = 0ms")

    add_heading_2("4.2 Verification Screenshot")
    add_image_with_caption("WhatsApp Image 2026-10-05 at 10.00.32 PM.jpeg", "Figure 4.1: Command prompt on PC0 showing successful 4/4 ICMP ping response from PC9 (0% packet loss)", width=Inches(5.8))

    add_heading_2("4.3 Results & Performance Analysis")
    add_bullet(" 100% transmission success rate (4 packets sent, 4 received, 0 dropped).", "Packet Delivery Rate:")
    add_bullet(" Average round-trip time of 0ms (Maximum 1ms), confirming zero latency overhead across switch trunk link.", "Latency & Speed:")
    add_bullet(" Standard IPv6 default TTL of 128 indicates direct layer-2 LAN switching without passing through intermediate routers.", "TTL Value:")
    add_bullet(" Confirms that IPv6 subnets, host IP bindings, physical cabling, and Cisco switch forwarding tables are fully operational.", "Overall Conclusion:")

    # =========================================================
    # SECTION 5: CONCLUSION & KEY LEARNINGS
    # =========================================================
    add_heading_1("5. Conclusion & Key Learnings")
    
    add_body("In this lab assignment, our team successfully planned, mathematically derived, configured, and verified an IPv6 subnetted enterprise network topology in Cisco Packet Tracer. Key takeaways from this assignment include:")
    
    add_bullet(" Mastered calculating host bits, prefix expansion (/120 to /124), subnet pool counts, block size, and hexadecimal jump increments (0x10) for IPv6 addressing.", "IPv6 Mathematical Subnetting:")
    add_bullet(" Learned to assign static IPv6 addresses and prefix lengths across end-user PCs in Packet Tracer.", "Host Addressing Implementation:")
    add_bullet(" Implemented essential Cisco IOS CLI hardening steps, including hostname assignment, domain lookup suppression, MOTD legal banners, enable secret passwords, console/VTY access protection, and password encryption.", "Cisco Switch Infrastructure Hardening:")
    add_bullet(" Validated network reachability and packet forwarding across inter-switch crossover links using ICMP ping utilities and Packet Tracer PDU simulation tools.", "Network Verification & Diagnostics:")

    output_path = "IPv6_Subnetting_and_Switch_Configuration_Assignment.docx"
    doc.save(output_path)
    print(f"Document successfully created and saved to: {output_path}")

if __name__ == "__main__":
    create_assignment()

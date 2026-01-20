"""Professional PDF generator for HRV reports"""
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from datetime import datetime
import os
import re

def parse_markdown_bold(text):
    """Convert markdown bold (**text**) to HTML bold tags"""
    # Replace pairs of ** with <b> and </b>
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)

def generate_pdf_report(output_path, record_id, dataset, grade, metrics, clinical_summary, plot_path=None):
    """
    Generate a professional PDF report for HRV analysis
    
    Args:
        output_path: Path to save the PDF
        record_id: Record identifier
        dataset: Dataset name
        grade: Signal quality grade
        metrics: Dictionary of HRV metrics
        clinical_summary: AI-generated clinical summary (markdown format)
        plot_path: Optional path to signal plot image
    """
    doc = SimpleDocTemplate(output_path, pagesize=letter,
                           rightMargin=0.75*inch, leftMargin=0.75*inch,
                           topMargin=0.75*inch, bottomMargin=0.75*inch)
    
    # Container for PDF elements
    elements = []
    
    # Custom styles
    styles = getSampleStyleSheet()
    
    # Title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Heading style
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=12,
        spaceBefore=16,
        fontName='Helvetica-Bold'
    )
    
    # Body style
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        textColor=colors.HexColor('#34495e'),
        alignment=TA_JUSTIFY,
        spaceAfter=12,
        leading=16
    )
    
    # Bullet style
    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['BodyText'],
        fontSize=11,
        textColor=colors.HexColor('#34495e'),
        leftIndent=20,
        spaceAfter=8,
        bulletIndent=10,
        leading=14
    )
    
    # === HEADER ===
    elements.append(Paragraph("HRV Analysis Report", title_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # === METADATA TABLE ===
    grade_color = colors.HexColor('#28a745') if grade == 'A' else colors.HexColor('#ffc107') if grade == 'B' else colors.HexColor('#dc3545')
    
    metadata = [
        ['Record ID:', record_id, 'Dataset:', dataset],
        ['Analysis Date:', datetime.now().strftime('%Y-%m-%d %H:%M'), 'Signal Grade:', grade],
    ]
    
    meta_table = Table(metadata, colWidths=[1.5*inch, 2*inch, 1.5*inch, 2*inch])
    meta_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#2c3e50')),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (2, 0), (2, -1), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#bdc3c7')),
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#ecf0f1')),
        ('BACKGROUND', (2, 0), (2, -1), colors.HexColor('#ecf0f1')),
        ('BACKGROUND', (3, 1), (3, 1), grade_color),
        ('TEXTCOLOR', (3, 1), (3, 1), colors.white),
        ('FONTNAME', (3, 1), (3, 1), 'Helvetica-Bold'),
    ]))
    
    elements.append(meta_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # === HRV METRICS TABLE ===
    elements.append(Paragraph("Heart Rate Variability Metrics", heading_style))
    
    metric_data = [
        ['Metric', 'Value', 'Unit', 'Interpretation'],
        ['Mean HR', f"{metrics.get('mean_hr', 'N/A'):.1f}" if isinstance(metrics.get('mean_hr'), (int, float)) else 'N/A', 'BPM', 'Average Heart Rate'],
        ['SDNN', f"{metrics.get('sdnn', 'N/A'):.1f}" if isinstance(metrics.get('sdnn'), (int, float)) else 'N/A', 'ms', 'Total HRV Power'],
        ['RMSSD', f"{metrics.get('rmssd', 'N/A'):.1f}" if isinstance(metrics.get('rmssd'), (int, float)) else 'N/A', 'ms', 'Vagal Tone'],
        ['pNN50', f"{metrics.get('pnn50', 'N/A'):.1f}" if isinstance(metrics.get('pnn50'), (int, float)) else 'N/A', '%', 'Parasympathetic Activity'],
        ['LF/HF Ratio', f"{metrics.get('lf_hf_ratio', 'N/A'):.2f}" if isinstance(metrics.get('lf_hf_ratio'), (int, float)) else 'N/A', '-', 'Autonomic Balance'],
    ]
    
    metrics_table = Table(metric_data, colWidths=[1.5*inch, 1.2*inch, 0.8*inch, 3.5*inch])
    metrics_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#3498db')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#bdc3c7')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))
    
    elements.append(metrics_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # === CLINICAL SUMMARY ===
    elements.append(Paragraph("Clinical Analysis", heading_style))
    elements.append(Spacer(1, 0.1*inch))
    
    # Parse the markdown-style summary and convert to PDF format with better styling
    summary_lines = clinical_summary.split('\n')
    in_bullet_section = False
    
    for line in summary_lines:
        line = line.strip()
        if not line:
            elements.append(Spacer(1, 0.05*inch))
            continue
        
        # Skip main title markers
        if line.startswith('# '):
            continue
        elif line.startswith('## '):
            # Sub-heading with improved style
            subheading = line.replace('##', '').strip().replace('📊', '').replace('🩺', '').replace('💡', '').strip()
            subheading_style = ParagraphStyle(
                'Subheading',
                parent=heading_style,
                fontSize=13,
                textColor=colors.HexColor('#2c3e50'),
                spaceAfter=6,
                spaceBefore=10,
                fontName='Helvetica-Bold'
            )
            elements.append(Paragraph(subheading, subheading_style))
            in_bullet_section = True
        elif line.startswith('- **') or line.startswith('* **'):
            # Bold bullet point
            bullet_text = line[2:].strip()
            bullet_text = parse_markdown_bold(bullet_text)
            
            enhanced_bullet_style = ParagraphStyle(
                'EnhancedBullet',
                parent=bullet_style,
                fontSize=10.5,
                leftIndent=15,
                bulletIndent=5,
                spaceAfter=6,
                leading=15
            )
            elements.append(Paragraph(f"• {bullet_text}", enhanced_bullet_style))
        elif line.startswith('- ') or line.startswith('* '):
            # Regular bullet point
            bullet_text = line[2:].strip()
            elements.append(Paragraph(f"• {bullet_text}", bullet_style))
        else:
            # Regular paragraph with better formatting
            formatted_line = parse_markdown_bold(line)
            para_style = ParagraphStyle(
                'FormattedBody',
                parent=body_style,
                fontSize=10.5,
                spaceAfter=10,
                leading=15
            )
            elements.append(Paragraph(formatted_line, para_style))
    
    elements.append(Spacer(1, 0.4*inch))
    
    # === SIGNAL VISUALIZATION ===
    if plot_path and os.path.exists(plot_path):
        elements.append(Paragraph("Signal Visualization", heading_style))
        elements.append(Spacer(1, 0.15*inch))
        
        # Add centered, properly scaled image
        try:
            img = Image(plot_path)
            # Scale to fit nicely on page
            img_width = 6.5 * inch
            img_height = 4.5 * inch
            img.drawWidth = img_width
            img.drawHeight = img_height
            
            # Center the image
            img.hAlign = 'CENTER'
            elements.append(img)
        except Exception as e:
            elements.append(Paragraph(f"Could not load visualization image.", body_style))
    
    # === FOOTER ===
    elements.append(Spacer(1, 0.4*inch))
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.HexColor('#95a5a6'),
        alignment=TA_CENTER,
        spaceAfter=4
    )
    elements.append(Paragraph("<b>HRV Coach Pro v2.1</b> | Powered by DeepSeek V3.2", footer_style))
    elements.append(Paragraph("For Educational and Research Purposes Only", footer_style))
    elements.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}", footer_style))
    
    # Build PDF
    doc.build(elements)
    return output_path

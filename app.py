import streamlit as st
import pandas as pd
import re
from io import StringIO

# Page config
st.set_page_config(
    page_title="Funeral Home Director Decoder",
    page_icon="🕊️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #2C3E50 0%, #34495E 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        background: linear-gradient(90deg, #3498DB 0%, #2980B9 100%);
        padding: 1rem;
        border-radius: 8px;
        color: white;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #FFF3CD;
        border: 1px solid #FFEAA7;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .tip-box {
        background-color: #D1ECF1;
        border: 1px solid #BEE5EB;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .red-flag {
        background-color: #F8D7DA;
        border: 1px solid #F5C6CB;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    .sidebar .sidebar-content {
        background-color: #F8F9FA;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🕊️ Navigation")
page = st.sidebar.selectbox(
    "Choose a section:",
    ["🏠 Home", "🧠 Psychology", "🛡️ Defense Strategies", "🚩 Red Flags", 
     "📚 Glossary", "📋 Meeting Prep", "📄 Document Analyzer"]
)

# Helper functions
def create_section_header(title, emoji):
    st.markdown(f"""
    <div class="section-header">
        <h2>{emoji} {title}</h2>
    </div>
    """, unsafe_allow_html=True)

def create_warning_box(content):
    st.markdown(f"""
    <div class="warning-box">
        <strong>⚠️ Warning:</strong> {content}
    </div>
    """, unsafe_allow_html=True)

def create_tip_box(content):
    st.markdown(f"""
    <div class="tip-box">
        <strong>💡 Tip:</strong> {content}
    </div>
    """, unsafe_allow_html=True)

def create_red_flag(content):
    st.markdown(f"""
    <div class="red-flag">
        <strong>🚩</strong> {content}
    </div>
    """, unsafe_allow_html=True)

# HOME PAGE
if page == "🏠 Home":
    # Main header
    st.markdown("""
    <div class="main-header">
        <h1>🕊️ Funeral Home Director Decoder</h1>
        <h3>Navigate funeral costs during your most vulnerable time</h3>
        <p><em>"Don't Get Sold - Get Decoded"</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💰 **The Hard Truth About Funeral Costs**")
        st.write("""
        The average funeral costs $7,000-$15,000, but families often pay much more due to:
        - **300-500% markup** on caskets
        - **Unnecessary** "protective" features
        - **Bundled packages** that prevent comparison shopping
        - **Emotional manipulation** during grief
        - **Financing schemes** with high interest rates
        """)
        

    
    with col2:
        st.markdown("### 🛠️ **How This App Protects You**")
        st.write("""
        **🧠 Psychology** - Understand manipulation tactics used during grief
        
        **🛡️ Defense Strategies** - Practical ways to protect yourself
        
        **🚩 Red Flags** - Warning signs of predatory practices
        
        **📚 Glossary** - Decode confusing funeral industry terms
        
        **📋 Meeting Prep** - Tools to prepare for funeral home visits
        
        **📄 Document Analyzer** - Upload quotes for instant analysis
        """)
    
    create_warning_box("""
    Funeral directors often exploit grief and time pressure. This app gives you the 
    knowledge to make informed decisions and avoid being taken advantage of during 
    one of life's most difficult times.
    """)

# PSYCHOLOGY PAGE
elif page == "🧠 Psychology":
    create_section_header("Understanding Grief Manipulation", "🧠")
    
    st.markdown("### How Funeral Directors Exploit Grief")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### **Time Pressure Tactics**")
        st.write("""
        - **"We need to move quickly"** - Creates artificial urgency
        - **Limited viewing hours** - Rushes decision-making
        - **"The body is deteriorating"** - Pressures immediate embalming
        - **Same-day decisions** - Prevents comparison shopping
        """)
        
        st.markdown("#### **Guilt and Shame Manipulation**")
        st.write("""
        - **"Don't you want the best for Mom?"** - Implies cheaper = less loving
        - **"This is your last gift to them"** - Emotional blackmail
        - **"What would they have wanted?"** - Guilt about budget concerns
        - **"Other families choose this"** - Social pressure
        """)
    
    with col2:
        st.markdown("#### **Authority and Expertise**")
        st.write("""
        - **Medical terminology** - Makes unnecessary services sound essential
        - **"Industry standard"** - Implies you have no choice
        - **"Legal requirement"** - Often false or misleading
        - **Professional appearance** - Builds unwarranted trust
        """)
        
        st.markdown("#### **Package Psychology**")
        st.write("""
        - **"Complete packages"** - Hides individual item costs
        - **Good/Better/Best tiers** - Anchors you to middle option
        - **"Included services"** - Makes unnecessary items seem free
        - **Upgrade pressure** - "Just a little more for..."
        """)
    
    create_tip_box("""
    Remember: Grief clouds judgment. Funeral directors are trained to recognize 
    and exploit emotional vulnerability. Understanding these tactics helps you 
    maintain perspective during difficult decisions.
    """)

# DEFENSE STRATEGIES PAGE
elif page == "🛡️ Defense Strategies":
    create_section_header("Protecting Yourself and Your Wallet", "🛡️")
    
    tab1, tab2, tab3 = st.tabs(["💪 Before You Go", "🤝 During Meetings", "📝 After Decisions"])
    
    with tab1:
        st.markdown("### **Preparation is Your Best Defense**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### **Research First**")
            st.write("""
            - **Compare 3+ funeral homes** before deciding
            - **Check online reviews** and Better Business Bureau ratings  
            - **Get price lists** over the phone (legally required)
            - **Understand your state's laws** about embalming requirements
            """)
            
            st.markdown("#### **Set Your Budget**")
            st.write("""
            - **Decide maximum spending** before you're emotional
            - **Consider cremation** - often 50-70% less expensive
            - **Research veteran benefits** if applicable
            - **Check life insurance** funeral benefits
            """)
        
        with col2:
            st.markdown("#### **Bring Support**")
            st.write("""
            - **Never go alone** - bring a clear-headed friend/family member
            - **Designate a 'bad cop'** - someone to ask hard questions
            - **Prepare questions in advance** - emotions cloud memory
            - **Take notes** during all conversations
            """)
            
            st.markdown("#### **Know Your Rights**")
            st.write("""
            - **You can buy caskets elsewhere** - funeral home cannot refuse
            - **Embalming is rarely required** by law
            - **You have 72 hours** to change your mind on contracts
            - **Itemized pricing** is legally required
            """)
    
    with tab2:
        st.markdown("### **During Funeral Home Meetings**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### **Key Phrases to Use**")
            st.write("""
            - **"Show me the itemized price list"**
            - **"What exactly is legally required?"**
            - **"I need to compare options before deciding"**
            - **"Can you break down this package?"**
            - **"What's the least expensive option?"**
            """)
            
            st.markdown("#### **Questions to Ask**")
            st.write("""
            - **"Why is embalming necessary?"** (often it's not)
            - **"Can I buy the casket elsewhere?"** (yes, you can)
            - **"What happens if I choose cremation?"**
            - **"What are your financing terms?"**
            - **"Can I get this in writing?"**
            """)
        
        with col2:
            st.markdown("#### **Red Flag Responses**")
            st.write("""
            - **"Trust me, this is what you need"**
            - **"We can't do the service without this"**
            - **"Other families always choose this"**
            - **"You don't want to think about money now"**
            - **"This is legally required"** (verify independently)
            """)
            
            st.markdown("#### **Take Control**")
            st.write("""
            - **Ask to see the casket room last** - prices will shock you into cheaper options
            - **Request written estimates** for everything
            - **Don't sign anything immediately** - take time to review
            - **Ask about payment plans** instead of financing
            """)
    
    with tab3:
        st.markdown("### **After Making Decisions**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### **Review Everything**")
            st.write("""
            - **Read contracts carefully** before signing
            - **Verify all charges** match what was discussed
            - **Understand cancellation policies**
            - **Keep copies** of all documents
            """)
        
        with col2:
            st.markdown("#### **You Can Still Make Changes**")
            st.write("""
            - **72-hour right** to modify contracts in many states
            - **Downgrade services** if you've overspent
            - **Cancel unnecessary add-ons**
            - **Switch funeral homes** if needed (with some restrictions)
            """)

# RED FLAGS PAGE
elif page == "🚩 Red Flags":
    create_section_header("Warning Signs of Predatory Practices", "🚩")
    
    tab1, tab2, tab3 = st.tabs(["💸 Pricing Red Flags", "🎭 Behavior Red Flags", "📄 Contract Red Flags"])
    
    with tab1:
        st.markdown("### **Pricing and Cost Red Flags**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            create_red_flag("**Refuses to provide price list** over phone (legally required)")
            create_red_flag("**Package pricing only** - won't break down individual costs")
            create_red_flag("**Casket prices over $3,000** - likely 400%+ markup")
            create_red_flag("**'Protective' casket features** - sealer gaskets, 'eternal' vaults")
            create_red_flag("**Expensive embalming** presented as legally required")
            create_red_flag("**Financing with interest rates** over 10%")
        
        with col2:
            create_red_flag("**'Service fees'** that aren't explained clearly")
            create_red_flag("**Charges for 'basic services'** that seem excessive")
            create_red_flag("**Mandatory packages** - 'you can't pick individual items'")
            create_red_flag("**Pressure to upgrade** during emotional moments")
            create_red_flag("**Hidden fees** not disclosed upfront")
            create_red_flag("**Cash-only or immediate payment** requirements")
    
    with tab2:
        st.markdown("### **Behavior and Communication Red Flags**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            create_red_flag("**Rushes you through decisions** - 'we need to decide today'")
            create_red_flag("**Uses guilt and shame** - 'don't you want the best for them?'")
            create_red_flag("**Dismisses budget concerns** - 'you can't put a price on love'")
            create_red_flag("**Claims everything is 'required by law'** without specifics")
            create_red_flag("**Discourages comparison shopping** - 'we're the best choice'")
            create_red_flag("**Won't let you bring advocates** or support people")
        
        with col2:
            create_red_flag("**Avoids answering direct questions** about costs or alternatives")
            create_red_flag("**Uses medical terminology** to confuse or intimidate")
            create_red_flag("**Pressures immediate signing** of contracts")
            create_red_flag("**Shows expensive options first** - anchoring technique")
            create_red_flag("**Claims 'other families always choose this'** - social pressure")
            create_red_flag("**Becomes defensive** when questioned about pricing")
    
    with tab3:
        st.markdown("### **Contract and Documentation Red Flags**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            create_red_flag("**Contracts with unclear language** or fine print")
            create_red_flag("**No itemized breakdown** of services and costs")
            create_red_flag("**Restrictive cancellation policies** - no cooling-off period")
            create_red_flag("**Automatic upgrades** written into contracts")
            create_red_flag("**Vague service descriptions** - what exactly are you paying for?")
            create_red_flag("**Payment terms** that seem predatory or excessive")
        
        with col2:
            create_red_flag("**No written estimate** provided before signing")
            create_red_flag("**Pressure to sign immediately** - 'this price expires today'")
            create_red_flag("**Additional fees** not mentioned until contract signing")
            create_red_flag("**Binding arbitration clauses** - limits your legal options")
            create_red_flag("**Automatic financing enrollment** without clear explanation")
            create_red_flag("**Changes to agreed prices** after initial discussion")

# GLOSSARY PAGE
elif page == "📚 Glossary":
    create_section_header("Funeral Industry Terms Decoded", "📚")
    
    st.markdown("### **Don't Let Confusing Terms Fool You**")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### **Casket & Burial Terms**")
        
        with st.expander("**Casket vs. Coffin**"):
            st.write("**Casket:** Rectangular, hinged lid. **Coffin:** Tapered, removable lid. Functionally identical - casket sounds fancier and costs more.")
        
        with st.expander("**Protective/Sealer Casket**"):
            st.write("**Reality:** Gasket that's supposed to keep out water/air. **Truth:** Bodies decompose regardless. Adds $500-2000 for no benefit.")
        
        with st.expander("**Burial Vault/Grave Liner**"):
            st.write("**Vault:** Concrete/metal container for casket. **Truth:** Required by cemeteries to prevent ground settling, NOT by law. Basic liner works fine.")
        
        with st.expander("**Memorial Package**"):
            st.write("**Sounds like:** A thoughtful collection. **Reality:** Bundled services at inflated prices to prevent comparison shopping.")
    
    with col2:
        st.markdown("#### **Service & Process Terms**")
        
        with st.expander("**Embalming**"):
            st.write("**Claimed:** Required by law. **Truth:** Only required for certain situations (public viewing after 24-48 hours, transport across state lines). Costs $500-800.")
        
        with st.expander("**Restoration**"):
            st.write("**Sounds like:** Necessary medical procedure. **Reality:** Cosmetic work that may be unnecessary, especially for closed-casket services.")
        
        with st.expander("**Basic Services Fee**"):
            st.write("**Claimed:** Overhead costs. **Reality:** Non-declinable fee ($1,500-3,000) that funeral homes use to inflate base costs.")
        
        with st.expander("**Direct Burial/Cremation**"):
            st.write("**Definition:** Body burial/cremation without ceremony. **Benefit:** Least expensive option, often 50-80% less than 'traditional' funeral.")
    
    st.markdown("#### **Financial Terms That Should Worry You**")
    
    col3, col4 = st.columns(2)
    
    with col3:
        with st.expander("**Pre-Need Contract**"):
            st.write("**Pitch:** Lock in today's prices. **Risks:** Company may go out of business, contracts may not transfer, inflation may outpace 'savings.'")
        
        with st.expander("**Assignment of Benefits**"):
            st.write("**Meaning:** Funeral home gets insurance money directly. **Risk:** You lose negotiating power and oversight of charges.")
    
    with col4:
        with st.expander("**Cash Advance Items**"):
            st.write("**Claimed:** Pass-through costs (flowers, newspaper notices). **Reality:** Often marked up 10-30% above actual cost.")
        
        with st.expander("**Immediate Need**"):
            st.write("**Used to justify:** Higher prices and pressure tactics. **Truth:** Most decisions can wait 24-48 hours for comparison shopping.")

# MEETING PREP PAGE
elif page == "📋 Meeting Prep":
    create_section_header("Prepare for Your Funeral Home Visit", "📋")
    
    tab1, tab2, tab3 = st.tabs(["📝 Before You Go", "❓ Questions to Ask", "📊 Comparison Tool"])
    
    with tab1:
        st.markdown("### **Pre-Meeting Checklist**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### **Research & Planning**")
            
            research_items = [
                "Get price lists from 3+ funeral homes",
                "Research your state's embalming laws",
                "Check veteran benefits eligibility",
                "Review life insurance funeral benefits",
                "Set maximum budget in advance",
                "Research cremation vs burial costs",
                "Find local casket retailers",
                "Check online reviews of funeral homes"
            ]
            
            for i, item in enumerate(research_items):
                if st.checkbox(item, key=f"research_{i}"):
                    st.success("✅ Completed")
        
        with col2:
            st.markdown("#### **Support System**")
            
            support_items = [
                "Choose a clear-headed advocate to attend",
                "Brief them on budget and preferences",
                "Assign them to ask tough questions",
                "Prepare list of questions together",
                "Plan to take notes during meeting",
                "Agree on decision-making timeline",
                "Exchange contact info with advocate",
                "Set post-meeting review time"
            ]
            
            for i, item in enumerate(support_items):
                if st.checkbox(item, key=f"support_{i}"):
                    st.success("✅ Completed")
    
    with tab2:
        st.markdown("### **Essential Questions to Ask**")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### **Legal Requirements**")
            questions_legal = [
                "What is actually required by law in our state?",
                "Is embalming legally required for our situation?", 
                "What are the minimum legal requirements for burial?",
                "What permits and documents do you handle?",
                "Can we purchase a casket from another retailer?",
                "What are our rights if we change our mind?"
            ]
            
            for q in questions_legal:
                st.write(f"• {q}")
            
            st.markdown("#### **Pricing & Costs**")
            questions_pricing = [
                "Can you provide an itemized price list?",
                "What is your least expensive burial option?",
                "What is your least expensive cremation option?",
                "Are there any additional fees not listed?",
                "What do other funeral homes charge for this?",
                "Can you break down this package into individual costs?"
            ]
            
            for q in questions_pricing:
                st.write(f"• {q}")
        
        with col2:
            st.markdown("#### **Services & Alternatives**")
            questions_services = [
                "What happens if we choose direct burial/cremation?",
                "Can we have a memorial service elsewhere?",
                "What less expensive casket options do you have?",
                "Why do you recommend embalming for our situation?",
                "What services can we decline or handle ourselves?",
                "Can family members participate in preparation?"
            ]
            
            for q in questions_services:
                st.write(f"• {q}")
            
            st.markdown("#### **Business Practices**")
            questions_business = [
                "What are your payment terms and options?",
                "Do you offer payment plans without interest?",
                "What is your policy on contract changes?",
                "Can we get this estimate in writing?",
                "How long do we have to make decisions?",
                "What happens if we choose another funeral home?"
            ]
            
            for q in questions_business:
                st.write(f"• {q}")
    
    with tab3:
        st.markdown("### **Funeral Home Comparison Tool**")
        
        st.write("Use this tool to compare quotes from multiple funeral homes:")
        
        # Create comparison table
        if 'comparison_data' not in st.session_state:
            st.session_state.comparison_data = {
                'Funeral Home': ['', '', ''],
                'Basic Services Fee': [0, 0, 0],
                'Casket Price': [0, 0, 0],
                'Embalming': [0, 0, 0],
                'Burial Vault': [0, 0, 0],
                'Cemetery Fee': [0, 0, 0],
                'Other Charges': [0, 0, 0]
            }
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### **Funeral Home 1**")
            st.session_state.comparison_data['Funeral Home'][0] = st.text_input("Name", key="name1")
            st.session_state.comparison_data['Basic Services Fee'][0] = st.number_input("Basic Services Fee", min_value=0, key="basic1")
            st.session_state.comparison_data['Casket Price'][0] = st.number_input("Casket Price", min_value=0, key="casket1") 
            st.session_state.comparison_data['Embalming'][0] = st.number_input("Embalming", min_value=0, key="emb1")
            st.session_state.comparison_data['Burial Vault'][0] = st.number_input("Burial Vault", min_value=0, key="vault1")
            st.session_state.comparison_data['Cemetery Fee'][0] = st.number_input("Cemetery Fee", min_value=0, key="cem1")
            st.session_state.comparison_data['Other Charges'][0] = st.number_input("Other Charges", min_value=0, key="other1")
            
            total1 = sum([st.session_state.comparison_data[key][0] for key in st.session_state.comparison_data.keys() if key != 'Funeral Home'])
            st.markdown(f"**Total: ${total1:,.2f}**")
        
        with col2:
            st.markdown("#### **Funeral Home 2**")
            st.session_state.comparison_data['Funeral Home'][1] = st.text_input("Name", key="name2")
            st.session_state.comparison_data['Basic Services Fee'][1] = st.number_input("Basic Services Fee", min_value=0, key="basic2")
            st.session_state.comparison_data['Casket Price'][1] = st.number_input("Casket Price", min_value=0, key="casket2")
            st.session_state.comparison_data['Embalming'][1] = st.number_input("Embalming", min_value=0, key="emb2")
            st.session_state.comparison_data['Burial Vault'][1] = st.number_input("Burial Vault", min_value=0, key="vault2")
            st.session_state.comparison_data['Cemetery Fee'][1] = st.number_input("Cemetery Fee", min_value=0, key="cem2")
            st.session_state.comparison_data['Other Charges'][1] = st.number_input("Other Charges", min_value=0, key="other2")
            
            total2 = sum([st.session_state.comparison_data[key][1] for key in st.session_state.comparison_data.keys() if key != 'Funeral Home'])
            st.markdown(f"**Total: ${total2:,.2f}**")
        
        with col3:
            st.markdown("#### **Funeral Home 3**")
            st.session_state.comparison_data['Funeral Home'][2] = st.text_input("Name", key="name3")
            st.session_state.comparison_data['Basic Services Fee'][2] = st.number_input("Basic Services Fee", min_value=0, key="basic3")
            st.session_state.comparison_data['Casket Price'][2] = st.number_input("Casket Price", min_value=0, key="casket3")
            st.session_state.comparison_data['Embalming'][2] = st.number_input("Embalming", min_value=0, key="emb3")
            st.session_state.comparison_data['Burial Vault'][2] = st.number_input("Burial Vault", min_value=0, key="vault3")
            st.session_state.comparison_data['Cemetery Fee'][2] = st.number_input("Cemetery Fee", min_value=0, key="cem3")
            st.session_state.comparison_data['Other Charges'][2] = st.number_input("Other Charges", min_value=0, key="other3")
            
            total3 = sum([st.session_state.comparison_data[key][2] for key in st.session_state.comparison_data.keys() if key != 'Funeral Home'])
            st.markdown(f"**Total: ${total3:,.2f}**")

# DOCUMENT ANALYZER PAGE
elif page == "📄 Document Analyzer":
    create_section_header("Analyze Funeral Home Quotes & Contracts", "📄")
    
    st.markdown("### **Upload Your Funeral Home Documents**")
    st.write("Upload quotes, estimates, or contracts for instant analysis of potential red flags and overcharges.")
    
    uploaded_file = st.file_uploader(
        "Choose a file", 
        type=['txt', 'pdf', 'doc', 'docx'],
        help="Upload funeral home quotes, contracts, or price lists"
    )
    
    if uploaded_file is not None:
        if uploaded_file.type == "text/plain":
            # Read text file
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            content = stringio.read()
            
            st.markdown("### **Document Analysis Results**")
            
            # Analyze the content
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### **🚩 Potential Red Flags Detected**")
                
                red_flags_found = []
                
                # Check for high-priced items
                if re.search(r'\$[0-9,]+', content):
                    prices = re.findall(r'\$([0-9,]+)', content)
                    for price in prices:
                        price_num = int(price.replace(',', ''))
                        if price_num > 3000:
                            red_flags_found.append(f"High-priced item: ${price} (likely significant markup)")
                
                # Check for suspicious terms
                suspicious_terms = [
                    ("protective", "Protective caskets often unnecessary"),
                    ("sealer", "Sealer gaskets provide no real benefit"), 
                    ("required", "Verify if actually legally required"),
                    ("package", "Bundled pricing prevents comparison"),
                    ("vault", "Basic grave liner may be sufficient"),
                    ("embalming", "Often not legally required"),
                    ("financing", "Check interest rates carefully"),
                    ("premium", "Premium features often overpriced")
                ]
                
                for term, warning in suspicious_terms:
                    if term.lower() in content.lower():
                        red_flags_found.append(warning)
                
                if red_flags_found:
                    for flag in red_flags_found[:10]:  # Limit to first 10
                        create_red_flag(flag)
                else:
                    st.success("No major red flags detected in this document.")
            
            with col2:
                st.markdown("#### **💡 Money-Saving Recommendations**")
                
                recommendations = [
                    "Ask for itemized pricing to compare individual services",
                    "Question if embalming is legally required for your situation", 
                    "Consider direct burial/cremation to save 50-70%",
                    "Shop for caskets at external retailers for potential savings",
                    "Ask about payment plans instead of financing options",
                    "Verify all 'required' services are actually mandated by law",
                    "Get quotes from 2-3 other funeral homes for comparison",
                    "Consider having memorial service at different location"
                ]
                
                for rec in recommendations:
                    st.write(f"• {rec}")
            
            st.markdown("#### **📄 Document Content Preview**")
            with st.expander("Click to view uploaded document"):
                st.text_area("Document Content", content, height=300)
        
        else:
            st.warning("PDF and Word document analysis coming soon. Please upload a text file for now.")
    
    st.markdown("### **Quick Price Check Tool**")
    st.write("Enter individual prices to check if they're reasonable:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        casket_price = st.number_input("Casket Price ($)", min_value=0, value=0)
        if casket_price > 0:
            if casket_price > 5000:
                st.error(f"🚩 Very high casket price. Markup likely 400-500%. Consider alternatives.")
            elif casket_price > 3000:
                st.warning(f"⚠️ High casket price. Significant markup likely.")
            else:
                st.success(f"✅ Reasonable casket price range.")
    
    with col2:
        embalming_price = st.number_input("Embalming Price ($)", min_value=0, value=0)
        if embalming_price > 0:
            if embalming_price > 800:
                st.error(f"🚩 Very high embalming price. Typical range: $400-700.")
            elif embalming_price > 600:
                st.warning(f"⚠️ Above average embalming price.")
            else:
                st.success(f"✅ Reasonable embalming price.")
    
    with col3:
        basic_fee = st.number_input("Basic Services Fee ($)", min_value=0, value=0)
        if basic_fee > 0:
            if basic_fee > 3000:
                st.error(f"🚩 Very high basic services fee. Typical range: $1,500-2,500.")
            elif basic_fee > 2500:
                st.warning(f"⚠️ Above average basic services fee.")
            else:
                st.success(f"✅ Reasonable basic services fee.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p><strong>Remember:</strong> You have rights as a consumer, even during grief. Don't let funeral directors pressure you into overspending.</p>
    <p><em>This tool is for educational purposes. Always verify legal requirements with your state's regulations.</em></p>
</div>
""", unsafe_allow_html=True)

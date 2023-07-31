import streamlit  as st 
 
def frontend():
    #sreamlit UI
    st.set_page_config(page_title="Chat with multiple pdf files!", layout="wide")
    st.title("Chat with Multiple :red[PDF Files]!")
    question = st.text_input("Ask questions Below: ")
   
    
    
    with st.sidebar:
        
        api_key = st.text_input("Enter apikey", placeholder="Enter openAI Key", type="password")
        
        st.subheader("Upload PDFs Here")
        
        pdfs = st.file_uploader("Upload PDF Files", type="pdf", accept_multiple_files=True) 
        
        st.button("Process")
    
    if pdfs and api_key is not None:
        if question:
            ans =comp_process(apikey=api_key, pdfs=pdfs, question=question)      
            st.text(ans)  
    
    
if __name__ =="__main__":
    frontend()
    
    
    
    
    


    



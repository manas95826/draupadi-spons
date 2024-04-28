import streamlit as st

# Dummy function to suggest speakers based on input
def suggest_speakers(topic):
    # Speaker data
    speakers = [
        {'name': 'Dr. Jane Smith', 'expertise': ['Artificial Intelligence', 'Machine Learning', 'Data Science'], 'contact': {'email': 'jane.smith@example.com', 'phone': '123-456-7890'}},
        {'name': 'Prof. Sarah Johnson', 'expertise': ['Environmental Science', 'Climate Change Policy'], 'contact': {'email': 'sarah.johnson@example.com', 'phone': '234-567-8901'}},
        {'name': 'Dr. Emily Davis', 'expertise': ['Psychology', 'Mental Health Awareness'], 'contact': {'email': 'emily.davis@example.com', 'phone': '345-678-9012'}},
        {'name': 'Dr. Maria Rodriguez', 'expertise': ['Astrophysics', 'Space Exploration'], 'contact': {'email': 'maria.rodriguez@example.com', 'phone': '456-789-0123'}}
    ]
    
    suggested_speakers = []
    for speaker in speakers:
        if topic in speaker['expertise']:
            suggested_speakers.append(speaker)
    
    return suggested_speakers

def main():
    st.title('Find Female Experts and Public Speakers')
    
    topic = st.text_input("Enter a topic of interest:")
    if topic:
        suggested_speakers = suggest_speakers(topic)
        if suggested_speakers:
            st.write(f"### Recommended Female Speakers for {topic}:")
            for speaker in suggested_speakers:
                st.write(f"**Name:** {speaker['name']}")
                st.write(f"**Expertise:** {', '.join(speaker['expertise'])}")
                st.write(f"**Contact:** Email: {speaker['contact']['email']}, Phone: {speaker['contact']['phone']}")
                st.write("---")
        else:
            st.write("No speakers found for the given topic.")

if __name__ == "__main__":
    main()

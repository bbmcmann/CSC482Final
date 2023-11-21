import Button from "@mui/material/Button";
import { useState } from "react";
import "./App.css";
import Biography from "./components/Biography";
import Resume, { ResumeProps } from "./components/Resume";

function App() {
  const [bio, setBio] = useState<string | undefined>();
  const [resume, setResume] = useState<ResumeProps | undefined>();

  const onClick = async () => {
    setBio(`I am a student at the Cal Poly SLO, studying Computer Science. I am
    interested in a wide variety of topics, including but not limited to:
    web development, machine learning, and natural language processing.`);
    setResume({
      name: "Jo Mama",
      email: "jomama@gmail.com",
      phone: "555-555-5555",
      linkedin: "linkedin.com/in/jomama",
      education: {
        school: "California Polytechnic State University, San Luis Obispo",
        location: "San Luis Obispo, CA",
        degree: "Bachelor of Science, Computer Science",
        gpa: 3.5,
        start: "September 2018",
        end: "June 2022",
        courses: [
          "Data Structures and Algorithms",
          "Systems Programming",
          "Computer Architecture and Assembly Language",
          "Operating Systems",
          "Artificial Intelligence",
          "Natural Language Processing",
          "Machine Learning",
        ],
      },
      experience: [
        {
          company: "Google",
          location: "Mountain View, CA",
          position: "Software Engineering Intern",
          start: "June 2021",
          end: "September 2021",
          description: [
            "Worked on the Google Search team",
            "Implemented a new feature for Google Search",
            "Used React, TypeScript, and Go",
          ],
        },
        {
          company: "Facebook",
          location: "Menlo Park, CA",
          position: "Software Engineering Intern",
          start: "June 2020",
          end: "September 2020",
          description: [
            "Worked on the Facebook Search team",
            "Implemented a new feature for Facebook Search",
            "Used React, TypeScript, and Go",
          ],
        },
      ],
      projects: [
        {
          name: "Artificial CSC Student",
          role: "Creator",
          start: "September 2021",
          end: "Present",
          description: "Created an artificial CSC student",
        },
        {
          name: "Artificial CSC Student",
          role: "Creator",
          start: "September 2021",
          end: "Present",
          description: "Created an artificial CSC student",
        },
      ],
      skills: [
        "Python",
        "Java",
        "C++",
        "JavaScript",
        "TypeScript",
        "React",
        "Go",
        "HTML",
        "CSS",
        "SQL",
        "Git",
      ],
    });
  };

  return (
    <div id="main">
      <h1>Artificial CSC Student</h1>
      <span>
        Created by Kelly Becker, Chris Kraft, Jonathan Laksana, & Ben McMann
      </span>
      <Button variant="contained" onClick={onClick}>
        Generate
      </Button>
      {bio && <Biography bio={bio} />}
      {resume && <Resume {...resume} />}
    </div>
  );
}

export default App;

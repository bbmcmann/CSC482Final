import Button from "@mui/material/Button";
import { useState } from "react";
import "./App.css";
import Biography from "./components/Biography";
import Resume, { ResumeProps } from "./components/Resume";

function App() {
  const [bio, setBio] = useState<string | undefined>();
  const [resume, setResume] = useState<ResumeProps | undefined>();

  const onClick = async () => {
    try {
      const response = await fetch("http://localhost:5000/generate");
      const data = await response.json();
      setBio(data.bio);
      setResume(data.resume);
    } catch (err) {
      console.error(err);
    }
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

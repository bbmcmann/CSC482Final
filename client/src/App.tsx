import {FormControl, FormControlLabel, InputLabel, MenuItem, Select, Switch} from "@mui/material";
import Button from "@mui/material/Button";
import { useRef, useState } from "react";
import "./App.css";
import Biography from "./components/Biography";
import Resume, { ResumeProps } from "./components/Resume";

function App() {
  const [bio, setBio] = useState<string | undefined>();
  const [resume, setResume] = useState<ResumeProps | undefined>();
  const [useCustomModel, setUseCustomModel] = useState<boolean>(false);
  const yearRef = useRef<HTMLSelectElement>();

  const onClick = async () => {
    try {
      const response = await fetch(
        "http://localhost:5000/generate?year=" + yearRef.current?.value
          + `&custom_model=${useCustomModel.toString()}`
      );
      const data = await response.json();
      setBio(data.bio);
      setResume(data.resume);
    } catch (err) {
      console.error(err);
    }
  };

  const onSwitch = () => {
    setUseCustomModel(!useCustomModel)
  }

  return (
    <div id="main">
      <h1>Artificial CSC Student</h1>
      <span>
        Created by Kelly Becker, Chris Kraft, Jonathan Laksana, & Ben McMann
      </span>
      <FormControl>
        <InputLabel id="year-label">Year</InputLabel>
        <Select
          labelId="year-label"
          defaultValue={6}
          inputRef={yearRef}
          label="Year"
          variant="outlined"
          color="primary"
          sx={{ width: 200, color: "#ddd" }}
        >
          <MenuItem value={1}>1</MenuItem>
          <MenuItem value={2}>2</MenuItem>
          <MenuItem value={3}>3</MenuItem>
          <MenuItem value={4}>4</MenuItem>
          <MenuItem value={5}>Graduate</MenuItem>
          <MenuItem value={6}>Random</MenuItem>
        </Select>
      </FormControl>

      <FormControlLabel
          control={<Switch checked={useCustomModel} onChange={onSwitch} />}
          label={"Use Custom Model"}
      />
          
      <Button variant="contained" onClick={onClick}>
        Generate
      </Button>
      {bio && <Biography bio={bio} />}
      {resume && <Resume {...resume} />}
    </div>
  );
}

export default App;

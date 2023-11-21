import Button from "@mui/material/Button";
import "./App.css";
import Biography from "./components/Biography";
import Resume from "./components/Resume";

function App() {
  return (
    <div id="main">
      <h1>Artificial CSC Student</h1>
      <Button variant="contained">Generate</Button>
      <Biography />
      <Resume />
    </div>
  );
}

export default App;

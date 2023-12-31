import { Button } from "@mui/material";
import {
  Document,
  Link,
  PDFViewer,
  Page,
  Text,
  View,
} from "@react-pdf/renderer";
import random from "random";
import { useEffect, useState } from "react";
import { getVariantStd } from "./resumeStyles";

export type ResumeProps = {
  year: number;
  name: string;
  email: string;
  phone: string;
  linkedin: string;
  education: {
    school: string;
    location: string;
    degree: string;
    gpa: number;
    start: string;
    end: string;
    courses: string[];
  };
  experience: {
    company: string;
    position: string;
    start: string;
    end: string;
    description: string[];
  }[];
  projects: {
    name: string;
    role: string;
    start: string;
    end: string;
    description: string[];
  }[];
  skills: {
    languages: string[];
    tools: string[];
  };
};

export default function Resume(props: ResumeProps) {
  const numEntries = props.experience.length + props.projects.length;
  const [styles, setStyles] = useState(getVariantStd(props.year, numEntries));

  const onClick = () => {
    setStyles(getVariantStd(props.year, numEntries));
  };

  useEffect(() => {
    setStyles(getVariantStd(props.year, numEntries));
  }, [props, numEntries]);

  const experienceSection = (
    <View style={styles?.section}>
      <Text style={styles?.sectionTitle}>Experience</Text>
      <View style={styles?.sectionContent}>
        {props.experience.map((exp) => (
          <View key={exp.company + exp.start} style={styles?.experienceSection}>
            <View style={styles?.rowPrim}>
              <Text style={styles?.sectionSubTitle}>{exp.position}</Text>
            </View>
            <View style={styles?.rowSec}>
              <Text style={styles?.sectionContentText}>{exp.company}</Text>
              <Text style={styles?.sectionContentText}>
                {exp.start} - {exp.end}
              </Text>
            </View>
            {exp.description.map((desc, i) => (
              <Text key={i} style={styles?.bulletPoint}>
                • {desc}
              </Text>
            ))}
          </View>
        ))}
      </View>
    </View>
  );

  const projectSection = (
    <View style={styles?.section}>
      <Text style={styles?.sectionTitle}>Projects/Outside Experience</Text>
      <View style={styles?.sectionContent}>
        {props.projects.map((proj) => (
          <View key={proj.role} style={styles?.experienceSection}>
            <View style={styles?.rowPrim}>
              <Text style={styles?.sectionSubTitle}>{proj.name}</Text>
              <Text style={styles?.sectionContentText}>
                {proj.start} - {proj.end}
              </Text>
            </View>
            {proj.role && (
              <View style={styles?.rowSec}>
                <Text style={styles?.sectionContentText}>{proj.role}</Text>
              </View>
            )}
            {proj.description.map((desc, i) => (
              <Text key={i} style={styles?.bulletPoint}>
                • {desc}
              </Text>
            ))}
          </View>
        ))}
      </View>
    </View>
  );

  const skillsSection = (
    <View style={styles?.section}>
      <Text style={styles?.sectionTitle}>Skills</Text>
      <View style={styles?.sectionContent}>
        <Text style={styles?.sectionSubTitle}>
          Languages:&nbsp;
          <Text style={styles?.sectionContentText}>
            {props.skills.languages.join(", ")}
          </Text>
        </Text>
        <Text style={styles?.sectionSubTitle}>
          Tools/Other:&nbsp;
          <Text style={styles?.sectionContentText}>
            {props.skills.tools.join(", ")}
          </Text>
        </Text>
      </View>
    </View>
  );

  const contentOrderHelper = () => {
    if (2 * props.experience.length >= props.projects.length) {
      return (
        <>
          {experienceSection}
          {projectSection}
        </>
      );
    } else {
      return <>{projectSection}</>;
    }
  };

  const contentOrder = () => {
    if (random.float() < 0.3) {
      return (
        <>
          {skillsSection}
          {contentOrderHelper()}
        </>
      );
    } else {
      return (
        <>
          {contentOrderHelper()}
          {skillsSection}
        </>
      );
    }
  };

  return (
    <div>
      <h3>Resume</h3>
      <Button variant="contained" onClick={onClick} sx={{ marginBottom: 2 }}>
        Randomize Style
      </Button>
      <PDFViewer style={styles?.viewer}>
        <Document title={`${props.name} Resume`}>
          <Page size="A4" style={styles?.page}>
            {/* HEADER SECTION */}
            <View style={styles?.header}>
              <Text style={styles?.name}>{props.name}</Text>
              <View style={styles?.headerline}>
                <Text style={styles?.contact}>
                  <Link src="https://www.google.com/">{props.email}</Link>
                </Text>
                <Text style={styles?.contact}>{props.phone}</Text>
                <Text style={styles?.contact}>
                  <Link src="https://www.google.com/">{props.linkedin}</Link>
                </Text>
              </View>
            </View>
            {/* EDUCATION SECTION */}
            <View style={styles?.section}>
              <Text style={styles?.sectionTitle}>Education</Text>
              <View style={styles?.sectionContent}>
                <View style={styles?.rowPrim}>
                  <Text style={styles?.sectionSubTitle}>
                    {props.education.school}
                  </Text>
                </View>
                <View style={styles?.rowSec}>
                  <Text style={styles?.sectionContentText}>
                    {props.education.degree}
                  </Text>
                  <Text style={styles?.sectionContentText}>
                    {props.education.start} - {props.education.end}
                  </Text>
                </View>
                {props.education.gpa > 3.0 ? (
                  <Text style={styles?.sectionContentText}>
                    GPA: {props.education.gpa}
                  </Text>
                ) : null}
                <Text style={styles?.sectionContentText}>
                  Relevant Courses: {props.education.courses.join(", ")}
                </Text>
              </View>
            </View>
            {contentOrder()}
          </Page>
        </Document>
      </PDFViewer>
    </div>
  );
}

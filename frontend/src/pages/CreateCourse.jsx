export default function CreateCourse() {
  const create = async () => {
    await fetch("http://localhost:8000/courses?topic=Test Course", {
      method: "POST"
    });
    alert("Course created");
  };

  return <button onClick={create}>Create Course</button>;
}

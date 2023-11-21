export default function Biography({ bio }: { bio: string }) {
  return (
    <div className="bio">
      <h3>Biography</h3>
      <p>{bio}</p>
    </div>
  );
}

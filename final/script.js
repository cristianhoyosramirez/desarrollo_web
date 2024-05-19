const requestOptions = {
  method: "GET",
  redirect: "follow"
};

fetch("https://dattebayo-api.onrender.com/teams", requestOptions)
  .then((response) => response.json())
  .then(result => displayTeams(result))
  .catch((error) => console.error(error));

function displayTeams(teams) {
  const teamsDiv = document.getElementById('teamsDiv');

  teams.teams.forEach(team => {
    const card = document.createElement('div');
    card.className = 'card';
    
    const cardTitle = document.createElement('div');
    cardTitle.className = 'card__title';

    const h1 = document.createElement('h1');
    h1.textContent = team.name;

    cardTitle.appendChild(h1);
    card.appendChild(cardTitle);
    teamsDiv.appendChild(card);
  });
}
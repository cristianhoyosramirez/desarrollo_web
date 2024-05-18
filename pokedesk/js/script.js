const requestOptions = {
    method: "GET",
    redirect: "follow"
};


const baseUrl = "https://pokeapi.co/api/v2/pokemon/";
let pokemons = document.getElementById('pokemons');
let prev = document.getElementById('prev');
let next = document.getElementById('next');

makeRequest(baseUrl, "getPokemons(data)");

function makeRequest(url, method) {

    fetch(url, requestOptions)
        .then((response) => response.json())
        .then((data) => eval(method))
        .catch((error) => console.error(error));
}

function getPokemons(data) {
    prev.dataset.prev = data.previous;
    next.dataset.next = data.next;

    data.results.forEach(pokemon => {
        makeRequest(pokemon.url, "createCard(data)")
    });
}

function createCard(data) {

    let name = data.name.toUpperCase();
    let imgUrl = data.sprites.other["official-artwork"].front_default;
    let stats= getStats(data.stats);

    pokemons.innerHTML += `
        <div class="card" onclick="showDetail('${name}','${imgUrl}','${stats}')">
            <div class="card__title">
                <h1>${name} </h1>
            </div>
        <img src="${imgUrl}" width="150rem" alt="">
    </div>
    `;
}

function getStats(stats){

    let skills="";

    stats.forEach( stat => {
        skills+=`<p><b>${stat.stat.name}:</b> ${stat.base_stat}</p>`
    })

    return skills;

} 

function showDetail(name,img,stats){
    Swal.fire({
        title: name,
        imageUrl: img,
        html:stats,
        width: 600,
        padding: "3em",
        color: "#716add",
        background: "#fff url(/images/trees.png)",
        showConfirmButton: false,
        backdrop: `
          rgba(0,0,123,0.4)
          url("assets/img/charmander.gif")
          left top
          no-repeat
        `
    });
}

prev.addEventListener('click', () => {
    update(prev.dataset.prev)
})

next.addEventListener('click', () => {
    update(next.dataset.next)
})


function update(url) {
    if (url !== 'null') {

        window.scroll({
            top: 0,
            left: 0,
            behavior: 'smooth'
        })
        pokemons.innerHTML = "";

        makeRequest(url, "getPokemons(data)");

    }

}

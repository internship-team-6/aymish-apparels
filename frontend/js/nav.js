var connectionParams = {
  method: "GET",
  mode: "cors",
  headers: {
    "Access-Control-Allow-Origin": "*",
    Accept: "application/json",
    "Content-Type": "application/json",
  },
};

const searchQuery = () => {
  const q = document.getElementById("searchid").value;
  window.location.href =
    "./search-product-list.html?" + new URLSearchParams({ q: q, page: 1 });
};

const categorySelect = (catlevel2NameObj) => {
  const catlevel2Id = catlevel2NameObj.value;
  window.location.href =
    "./category-product-list.html?" +
    new URLSearchParams({
      catlevel2Id: catlevel2Id,
      page: 1,
    });
};

window.onload = (() => {
  let nav = document.querySelector("#navbar");
  nav.innerHTML = `
    <div class="nav">
      <a href="index.html"><img src="img/final_logo.png" class="brand-logo" alt="" /></a>
      <div class="nav-items">
        <div class="search">
          <form class="form-bar">
            <input type="text" class="search-box" id="searchid" placeholder="search brand, product"/>
            <button class="search-btn" type="button" onclick="searchQuery()">search</button>
          </form>
        </div>
        
      </div>
    </div>
    <div class="cat" id="cat-level-1">
    </div>
    `;
  let searchIdInput = document.getElementById("searchid");
  searchIdInput.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      event.preventDefault();
      searchQuery();
    }
  });
  fetch("http://localhost:5000/navbar", connectionParams)
    .then((response) => response.json())
    .then((data) => {
      const categoriesArr = data;
      let catLevel1 = document.getElementById("cat-level-1");
      for (let counter = 0; counter < categoriesArr.length; counter++) {
        let catlevel1Name = categoriesArr[counter]["name"];
        let catlevel1Id = categoriesArr[counter]["id"];
        catLevel1.innerHTML += `
          <select name="${catlevel1Name}" id="${catlevel1Id}" onchange="categorySelect(this)">
            <option value="" selected disabled hidden>${catlevel1Name}</option>
            <option value="*">All</option>
          </select>
          `;
        fetch(
          "http://localhost:5000/dropdown?" +
            new URLSearchParams({ catlevel1Id: catlevel1Id }),
          connectionParams
        )
          .then((response) => response.json())
          .then((data) => {
            catLevel1IdElement = document.getElementById(catlevel1Id);
            let newInnerHTML = data
              .map((record) => {
                let val_id = record["id"];
                let val_name = record["name"];
                return `<option id="${val_id}" value="${val_id}">${val_name}</option>`;
              })
              .reduce((x, y) => x + y);
            catLevel1IdElement.innerHTML += newInnerHTML;
          });
      }
    });
})();

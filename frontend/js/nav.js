const searchQuery = function () {
  const q = document.getElementById("searchid").value;
  location.href =
    "./search-product-list.html?" + new URLSearchParams({ q: q, page: "1"});
};

const searchQuerySort = function (sort) {
  let params = new URLSearchParams(location.search);
  let q = params.get("q");
  location.href =
    "./search-product-list.html?" +
    new URLSearchParams({ q: q, page: "1", sort: sort.value });
};

const categorySelect = function (catlevel1Id, catlevel2NameObj) {
  const catlevel2Name = catlevel2NameObj.value;
  location.href =
    "./category-product-list.html?" +
    new URLSearchParams({
      catlevel1Id: catlevel1Id,
      catlevel2Name: catlevel2Name,
      page: "1",
    });
};

const categorySelectSort = function (sort) {
  let params = new URLSearchParams(location.search);
  let catlevel1Id = params.get("catlevel1Id");
  let catlevel2Name = params.get("catlevel2Name");
  location.href =
    "./category-product-list.html?" +
    new URLSearchParams({
      catlevel1Id: catlevel1Id,
      catlevel2Name: catlevel2Name,
      page: "1",
      sort: sort.value
    });
}

const navbarFunction = function () {
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
  fetch("http://localhost:5000/navbar", {
    method: "GET",
    mode: "cors",
    headers: {
      "Access-Control-Allow-Origin": "*",
      Accept: "application/json",
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const categories_arr = data;
      let cat_level_1 = document.getElementById("cat-level-1");
      for (let i = 0; i < categories_arr.length; i++) {
        let catlevel1Name = categories_arr[i]["name"];
        let catlevel1Id = categories_arr[i]["id"];
        cat_level_1.innerHTML += `
          <select name="${catlevel1Name}" id="${catlevel1Id}" onchange="categorySelect(${catlevel1Id}, this)">
            <option value="" selected disabled hidden>${catlevel1Name}</option>
            <option value="">All</option>
          </select>
        `;
        fetch(
          "http://localhost:5000/dropdown?" +
            new URLSearchParams({ catlevel1Id: catlevel1Id }),
          {
            method: "GET",
            mode: "cors",
            headers: {
              "Access-Control-Allow-Origin": "*",
              Accept: "application/json",
              "Content-Type": "application/json",
            },
          }
        )
          .then((response) => response.json())
          .then((data) => {
            cat_level_1_id_element = document.getElementById(catlevel1Id);
            for (let i = 0; i < data.length; i++) {
              let val = data[i]["name"];
              cat_level_1_id_element.innerHTML += `
                <option id="${val}" value="${val}">
                  ${val}
                </option>
              `;
            }
          });
      }
    });
};

onload = navbarFunction();

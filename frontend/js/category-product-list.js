var connectionParams = {
  method: "GET",
  mode: "cors",
  headers: {
    "Access-Control-Allow-Origin": "*",
    Accept: "application/json",
    "Content-Type": "application/json",
  },
};
var limit = 15;

const categorySelectSort = (sort) => {
  let params = new URLSearchParams(window.location.search);
  let catlevel2Id = params.get("catlevel2Id");
  window.location.href =
    "./category-product-list.html?" +
    new URLSearchParams({
      catlevel2Id: catlevel2Id,
      sort: sort.value,
      page: 1,
    });
};

window.onload = (() => {
  const queryString = window.location.search;
  const urlParams = new URLSearchParams(queryString);
  const page = parseInt(urlParams.get("page"));
  const offset = (page - 1) * limit;
  const catlevel2Id = urlParams.get("catlevel2Id");
  const sort = urlParams.get("sort");
  fetch(
    "http://localhost:5000/name-tree?" +
      new URLSearchParams({ catlevel2Id: catlevel2Id }),
    connectionParams
  )
    .then((response) => response.json())
    .then((data) => {
      let categoryPath = data.reduce((x, y) => x + "/" + y);
      document.getElementById(
        "path"
      ).innerHTML += `<a href="./index.html" style="text-decoration:none;color:#bf616a" margin-left=20px>Home</a>/${categoryPath}`;
      document.getElementById("product-query").innerHTML = categoryPath;
      document.title = "Product list for category" + categoryPath;
      document.getElementById("cat-title").innerHTML = catlevel2Id;
      let catParamsMap = { catlevel2Id: catlevel2Id };
      if (sort !== null && sort.length !== 0) {
        catParamsMap["sort"] = sort;
      }
      fetch(
        "http://localhost:5000/category-product-list?" +
          new URLSearchParams(catParamsMap),
        connectionParams
      )
        .then((response) => response.json())
        .then((data) => {
          const productsArr = data;
          let prodListDiv = document.getElementById("product-list-div");
          const newInnerHTML = productsArr
            .slice(offset, Math.min(offset + limit, productsArr.length))
            .map(
              (product) => `
          <div class="product-container" id="product-list-div" onclick = "window.open('product.html?uniqueId=${product["id"]}','_blank');">
            <div class="product-card">
              <div class="product-image">
                <img src="${product["image"]}" class="product-thumb product-border" alt="" />
              </div>
              <div class="product-info">
                <p class="product-title">${product["title"]}</p>
                <p class="price">$${product["price"]}</p>
              </div>
            </div>
          </div>
          `
            )
            .reduce((x, y) => x + y);
          prodListDiv.innerHTML += newInnerHTML;
          const pages =
            Math.floor(productsArr.length / limit) +
            (productsArr.length % limit && 1);
          let paginationId = document.getElementById("pagination");
          if (page !== 1) {
            let catParams = new URLSearchParams({
              ...catParamsMap,
              page: page - 1,
            });
            paginationId.innerHTML += `<a href="./category-product-list.html?${catParams}">&#10094;</a>`;
          }
          let paginationNewInnerHTMLArr = Array.from(
            { length: pages },
            (_, tempPage) => tempPage + 1
          ).map((tempPage) => {
            let catParams = new URLSearchParams({
              ...catParamsMap,
              page: tempPage,
            });
            return `<a href="./category-product-list.html?${catParams}">${tempPage}</a>`;
          });
          let catParams = new URLSearchParams({
            ...catParamsMap,
            page: page,
          });
          paginationNewInnerHTMLArr[
            page - 1
          ] = `<a class="active" href="./category-product-list.html?${catParams}">${page}</a>`;
          let paginationNewInnerHTML = paginationNewInnerHTMLArr.reduce(
            (x, y) => x + y
          );
          paginationId.innerHTML += paginationNewInnerHTML;
          if (page !== pages) {
            let catParams = new URLSearchParams({
              ...catParamsMap,
              page: page + 1,
            });
            paginationId.innerHTML += `<a href="./category-product-list.html?${catParams}">&#10095;</a>`;
          }
        });
    });
})();

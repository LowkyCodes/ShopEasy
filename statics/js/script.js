let meals = [];
let current = 0;

async function loadMeals() {
  const res = await fetch('/api/meals');
  meals = await res.json();
  showMeal();
}

function showMeal() {
  if (current < meals.length) {
    document.getElementById("meal-card").innerText = meals[current].name;
  } else {
    document.getElementById("meal-card").innerText = "No more meals to show!";
  }
}

function swipe(direction) {
  console.log(`Swiped ${direction} on ${meals[current].name}`);
  current++;
  showMeal();
}

loadMeals();

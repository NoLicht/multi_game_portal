document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.favorite-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const type = this.dataset.type;
            const id = this.dataset.id;
            fetch(`/database/toggle_favorite/${type}/${id}/`)
                .then(res => res.json())
                .then(data => {
                    if (data.favorited) this.textContent = '★';
                    else this.textContent = '☆';
                });
        });
    });
});

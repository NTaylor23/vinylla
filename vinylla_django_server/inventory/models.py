from django.db import models


class Release(models.Model):
    artist_name: models.CharField = models.CharField(
        blank=False, null=False, max_length=100
    )
    album_title: models.CharField = models.CharField(
        blank=False, null=False, max_length=1000
    )
    genre: models.CharField = models.CharField(max_length=50)
    style: models.CharField = models.CharField(max_length=50, blank=True)
    format: models.CharField = models.CharField(max_length=20)
    discogs_release_id: models.CharField = models.CharField(max_length=100)

    year: models.IntegerField = models.IntegerField()

    price: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=2)

    in_wantlist: models.BooleanField = models.BooleanField(default=False)

    image_url: models.URLField = models.URLField(null=True, blank=True)
    thumbnail_url: models.URLField = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        s = f"{self.artist_name} - {self.album_title}"
        if self.year:
            s += f" ({self.year})"
        return s


class Track(models.Model):
    release: models.ForeignKey = models.ForeignKey(Release, on_delete=models.CASCADE)
    track_title: models.CharField = models.CharField(
        blank=False, null=False, max_length=200
    )
    duration: models.CharField = models.CharField(blank=True, null=True, max_length=10)

    def __str__(self):
        return f"{self.release.artist_name} - {self.track_title}"

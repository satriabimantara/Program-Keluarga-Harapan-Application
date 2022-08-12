from django.db import models

# Create your models here.


class Kecamatan(models.Model):
    kode_kecamatan = models.CharField(
        'Kode Kecamatan',
        max_length=6,
        unique=True
    )
    nama_kecamatan = models.CharField(
        'Nama Kecamatan',
        max_length=25,
        unique=True
    )

    class Meta:
        ordering = ['kode_kecamatan']
        verbose_name_plural = "Kecamatan"

    def __str__(self):
        return "{} | {} ".format(
            self.kode_kecamatan, self.nama_kecamatan
        )


class Kelurahan(models.Model):
    kode_kelurahan = models.CharField(
        'Kode Kelurahan',
        max_length=6,
        unique=True
    )
    nama_kelurahan = models.CharField(
        'Nama Kelurahan',
        max_length=25,
        unique=True
    )

    class Meta:
        ordering = ['kode_kelurahan']
        verbose_name_plural = "Kelurahan"

    def __str__(self):
        return "{} | {} ".format(
            self.kode_kelurahan, self.nama_kelurahan
        )


class DataPenduduk(models.Model):
    nik = models.CharField(
        'Nomor Induk Kependudukan (KTP)',
        max_length=17,
        unique=True,
    )
    nama_lengkap = models.CharField(
        'Nama Lengkap Pengurus',
        max_length=100,
        unique=True
    )
    alamat = models.CharField(
        'Alamat Tempat Tinggal',
        max_length=150,
        null=True,
    )
    kelurahan = models.ForeignKey(
        Kelurahan,
        on_delete=models.SET_NULL,
        null=True
    )
    kecamatan = models.ForeignKey(
        Kecamatan,
        on_delete=models.SET_NULL,
        null=True
    )
    jumlah_anak_sd = models.PositiveSmallIntegerField(
        'Jumlah Anak SD',
    )
    jumlah_anak_smp = models.PositiveSmallIntegerField(
        'Jumlah Anak SMP',
    )
    jumlah_anak_sma = models.PositiveSmallIntegerField(
        'Jumlah Anak SMA',
    )
    jumlah_ibu_hamil = models.PositiveSmallIntegerField(
        'Jumlah Ibu Hamil',
    )
    jumlah_balita = models.PositiveSmallIntegerField(
        'Jumlah Anak Balita',
    )
    jumlah_balita_anakprasekolah = models.PositiveSmallIntegerField(
        'Jumlah Anak Balita dan Prasekolah',
    )
    jumlah_lanjut_usia = models.PositiveSmallIntegerField(
        'Jumlah Orang Lanjut Usia',
    )
    jumlah_penyandang_disabilitas = models.PositiveSmallIntegerField(
        'Jumlah Penyandang Disabilitas',
    )

    prediksi_bantuan = models.DecimalField(
        'Total Bantuan diterima (Rp.)',
        max_digits=20,
        decimal_places=4,
        null=True,
        blank=True,
    )
    published = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )
    updated = models.DateTimeField(
        auto_now=True,
        editable=False
    )

    class Meta:
        ordering = ['published']
        verbose_name_plural = "Penduduk"

    def __str__(self):
        return "{} | {} | {}".format(
            self.nik, self.nama_lengkap, self.prediksi_bantuan
        )

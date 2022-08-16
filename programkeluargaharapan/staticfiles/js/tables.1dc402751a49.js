$(document).ready(function(){
	/*INPUT DATA PAGE*/
	function inputDataTable(object){
		for (const keys in object) {
			$(object[keys].id).DataTable({
				scrollX: 300,
				scrollY: 300,
				"processing": true,
				autoWidth :true,
				buttons: [
				{
					extend :'pdfHtml5',
					className : 'btn-success',
					orientation :'landscape',
					text: '<i class="fas fa-file-pdf" aria-hidden="true"></i> PDF',
					title: object[keys].title,
					extension: ".pdf",
					filename: object[keys].filename
				}
				],
				"dom": `
				<'row mb-3' <'col-lg-6 d-flex justify-content-start' f> <'col-lg-6 d-flex justify-content-end' l>>+
                <'d-flex justify-content-end' B>+
				<'mb-3' t> +
				<'d-flex justify-content-start mb-5 mt-3'p>
				`
			});
		}
	}
	const table = {
		table_lihat_data : {
			id : "#table-lihat-data",
			title : "Program Keluarga Harapan Dataset",
			filename : "Program Keluarga Harapan Dataset"
		},
		table_data_latih : {
			id : "#table-data-latih",
			title : "Data Latih PKH 80%",
			filename : "Data Latih PKH 80%"
		},
		table_data_uji : {
			id : "#table-data-uji",
			title : "Data Uji PKH 20%",
			filename : "Data Uji PKH 20%"
		},
		table_data_penduduk : {
			id : "#table-penduduk",
			title : "Tabel Data Penduduk Baru",
			filename : "Tabel Data Penduduk Baru"
		},
	};
	inputDataTable(table);
});
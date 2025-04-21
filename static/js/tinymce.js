tinymce.init({
    selector: 'textarea',
    setup: function (editor) {
      editor.on('NodeChange', function () {
        const h2s = editor.getDoc().querySelectorAll('h2');
        h2s.forEach(h => h.className = 'text-3xl font-semibold mb-3');
      });
    }
  });
  
if (typeof jQuery === 'undefined' && django && django.jQuery) {
    jQuery = django.jQuery;
}

if (typeof redactor_custom_options === 'undefined') {
    redactor_custom_options = {}
}

(function($) {
    $(document).ready(function() {
        $(document).on('redactor:init', 'textarea.redactor-box', function() {
            var redactor_options = $.extend({}, $(this).data('redactor-options'),
                                            redactor_custom_options);
            if (typeof redactor_options.imageUploadErrorCallback === 'undefined') {
                redactor_options.imageUploadErrorCallback = function (json) {
                    alert(json.error);
                }
            }
            $(this).redactor(redactor_options);
        });
        $(document).trigger('redactorWidgetReady');

        $('textarea.redactor-box:not([id*="__prefix__"])').each(function() {
            $(this).trigger('redactor:init');
        });

        // Initialize Redactor on admin's dynamically-added inline
        // formsets.
        //
        // Credit to the approach taken in django-selectable:
        // https://github.com/mlavin/django-selectable
        $(document).on('click', '.add-row', function () {
            $(this).parents('.inline-related')
                   .find('tr.form-row:not(.empty-form)').last()
                   .find('textarea.redactor-box')
                   .trigger('redactor:init');
        });
    });
})(jQuery);

function pos_custom(instance, module){
  var QWeb = instance.web.qweb;

    module.CustomButtonWidget = module.ScreenWidget.extend({
      template: 'CustomButtonWidget',
      init: function(parent, options){
        this._super(parent);
      }

    });

    module.CustomPageWidget = module.ScreenWidget.extend({
      template:'CustomPageWidget',

      init: function(parent, options) {
        this._super(parent);
      },

      renderElement: function() {
        var self = this;
        this._super();

        self.afficherPage()
      },

      afficherPage: function(){
        var button = $(QWeb.render('CustomButtonWidget'));
        button.appendTo($('.control-buttons'));
        $('.control-buttons').removeClass('oe_hidden');
        $('.control-buttons').addClass('mypad');

        button.click(function(){
          $(QWeb.render('CustomPageWidget'));
          $('.page-list-container').removeClass('oe_hidden');
          $('.page-list').append("AZERTY");
          self.pos_widget.screen_selector.set_current_screen('my_page');
        })
      },

    });

}

(function(){
    var _super = window.openerp.point_of_sale;
    window.openerp.point_of_sale = function(instance){
        _super(instance);
        var module = instance.point_of_sale;
        pos_custom(instance, module);
    }
})();
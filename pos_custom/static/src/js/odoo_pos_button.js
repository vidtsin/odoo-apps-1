function pos_custom(instance, module){
  var QWeb = instance.web.qweb;

    module.CustomButtonWidget = module.ScreenWidget.extend({
      template: 'CustomButtonWidget',
      init: function(parent, options){
        this._super(parent);
      }

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
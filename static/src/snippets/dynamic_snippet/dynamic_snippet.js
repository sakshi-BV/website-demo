/** @odoo-module **/
import publicWidget from "web.public.widget"
import core from 'web.core'

var Dynamic_Qweb = core.qweb
publicWidget.registry.DynamicEmployeeCarousel = publicWidget.Widget.extend({
    selector: '.container',

    start() {
        this._rpc({
            route: "/employee/model",
            params: {}
        }).then((data) => {
            
            this.$target.replaceWith(Dynamic_Qweb.render("website_demo.emp_detail", {data: data}))
           
        });
    }
});
export default publicWidget.registry.DynamicEmployeeCarousel;
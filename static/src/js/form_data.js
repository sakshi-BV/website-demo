/** @odoo-module **/
import publicWidget from "web.public.widget"
import core from 'web.core'

publicWidget.registry.FormDataLoad = publicWidget.Widget.extend({
    selector: '#form_template',
    events : {
        'click #form_button' : 'on_submit', 
    },
    on_submit(){
        console.log(this.$el)
        let emp_name = this.$el.find('input#emp_name')[0].value
        let emp_city = this.$el.find('input#emp_city')[0].value
        let emp_work = this.$el.find('input#emp_work')[0].value
        let emp_phone = this.$el.find('input#emp_phone')[0].value
        console.log('data',emp_name,emp_city,emp_phone,emp_work)

        this._rpc({
            route: "/employee/data",
            params: {'emp_name': emp_name,
                    'city' : emp_city,
                    'work_experience': emp_work,
                    'phone_number' : emp_phone,    
                }
        }).then((data) => {
            console.log(data)                    
        });
    }

   
});
export default publicWidget.registry.FormDataLoad;
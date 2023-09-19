/** @odoo-module **/
import publicWidget from "web.public.widget"
// import core from 

publicWidget.registry.FormDataLoad = publicWidget.Widget.extend({
    selector: '#mysection',
    events: {
        'click #form_button': 'on_submit',
        'click button#popup-login': function () {
            var link = $('button#popup-login').data('link');
            if (link) {
                window.location.href = link;
            }
        }
    },

    on_submit() {
        function popup(el, title = "title", msg = "nothing", button_name = null, link = null) {
            var popup_el = el.find('div#exampleModal');
            var popup_title = el.find('h1#exampleModalLabel')[0]
            var popup_msg = el.find('div#popup-body')[0]
            var popup_ok = el.find('button#popup-login')
            
            popup_title.innerHTML = title
            popup_msg.innerHTML = msg
            if (link != null && button_name != null) {
                popup_ok[0].innerHTML = button_name
                popup_ok.attr('data-link', link);
            } else {
                popup_ok[0].style.display = 'none'
            }
            popup_el.modal('show');
        }
        console.log(this.getSession().user, 'aaaaaaaaaaaaaaaa')
        console.log(this.$el)
        // debugger
        let emp_name = this.$el.find('input#emp_name')[0].value
        // let emp_name = this.$el.find('input#emp_name')[0].value
        let emp_city = this.$el.find('input#emp_city')[0].value
        let emp_work = this.$el.find('input#emp_work')[0].value
        let emp_phone = this.$el.find('input#emp_phone')[0].value
        console.log('data', emp_name, emp_city, emp_phone, emp_work)


        if (this.getSession().user_id) {

            if (!emp_name || !emp_city || !emp_work || !emp_phone) {
                popup(this.$el, 'Alert', 'Please fill all the fields')
            }

            else {

                this._rpc({
                    route: "/employee/data",
                    params: {
                        'emp_name': emp_name,
                        'city': emp_city,
                        'work_experience': emp_work,
                        'phone_number': emp_phone,
                    }
                }).then((data) => {
                    console.log(data)
                    // alert("Form submitted successfully!");
                    popup(this.$el,'Success','saved successfully')
                });
            }
        }
        else{
            popup(this.$el, 'Login', 'You are not Login', 'Sign In', 'http://localhost:8069/web/login')
        }
    }
});
export default publicWidget.registry.FormDataLoad;


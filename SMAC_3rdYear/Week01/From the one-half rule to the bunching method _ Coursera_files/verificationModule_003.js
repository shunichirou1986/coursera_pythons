define("bundles/verification/viewModels/verificationModule",["require","exports","module","backbone","underscore","bundles/ondemand/utils/assignmentVerificationTest","bundles/phoenix/template/models/userVerification","js/constants/userAgent","js/lib/fsm"],function(require,exports,module){"use strict";var Backbone=require("backbone"),_=require("underscore"),t=require("bundles/ondemand/utils/assignmentVerificationTest"),i=t.inHonorCodeVariant,e=require("bundles/phoenix/template/models/userVerification"),n=require("js/constants/userAgent"),s=require("js/lib/fsm"),o=Backbone.Model.extend(_.extend({},s.FiniteStateMachine,{logTransitions:!0,defaults:{state:"none",activeViewModel:null,verifiableId:null},fsm:{states:["none","block-verification","registration","verification","honor-code"],transitions:{"block-verification":["none"],"honor-code":["none"],registration:["none","block-verification"],verification:["none","block-verification"]}},initialize:function initialize(i){this.metadata=i.metadata,this.set("canOptOut",i.canOptOut),this.set("isMobile",n.isMobile),this.set("isProfileComplete",e.canVerifyCoursework()),i.verificationDisplay?(this.set("isVerifyingAssessment",!0),this.productOwnership=i.verificationDisplay.get("productOwnership"),this.verificationPreferences=i.verificationDisplay.get("verificationPreferences"),this.set("hasPaidForVerification",this.productOwnership.get("owns")),this.set("optedOutOfVerification",this.verificationPreferences.get("optedOutOfVerification")),this.set("canOptOut",!this.get("hasPaidForVerification")),this.selectVerificationFlow()):(this.set("isVerifyingAssessment",!1),this.get("isMobile")?(this.set("optedOutOfVerification",!1),this.transition("block-verification")):this.transition("registration"))},selectVerificationFlow:function selectVerificationFlow(){this.get("isMobile")||this.get("optedOutOfVerification")?this.transition("block-verification"):i()?this.transition("honor-code"):this.get("isProfileComplete")?this.transition("verification"):this.transition("registration")},unblockVerification:function unblockVerification(){i()?this.transition("honor-code"):this.get("isProfileComplete")?this.transition("verification"):this.transition("registration")}}));module.exports=o});
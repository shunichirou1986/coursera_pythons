define("pages/open-course/peerReview/views/preview",["require","exports","module","jquery","origami","underscore","bundles/phoenix/lib/eventDefinitions","bundles/phoenix/lib/view","bundles/phoenix/views/loading","js/app/scrollTrackerSingleton","js/lib/flashmessage","js/lib/path","js/lib/pluralize","pages/open-course/peerReview/components/alerts/views/alerts","pages/open-course/peerReview/components/submissionHeader/views/submissionHeader","pages/open-course/peerReview/submissionTypes/getSubmissionTypeConfig","pages/open-course/peerReview/viewModels/preview","pages/open-course/peerReview/views/alerts/submitSuccess.graded.html","pages/open-course/peerReview/views/alerts/submitSuccess.ungraded.html","pages/open-course/peerReview/views/preview.html","pages/open-course/peerReview/views/rubricQuestions","pages/open-course/peerReview/views/submissionError.html","pages/open-course/peerReview/views/submissionWarning.html","bundles/verification/viewModels/verificationModule","bundles/verification/views/verificationModule"],function(require,exports,module){"use strict";var $=require("jquery"),t=require("origami"),_=require("underscore"),i=require("bundles/phoenix/lib/eventDefinitions"),p=require("bundles/phoenix/lib/view"),o=require("bundles/phoenix/views/loading"),u=require("js/app/scrollTrackerSingleton"),d=require("js/lib/flashmessage"),e=require("js/lib/path"),v=require("js/lib/pluralize"),n=require("pages/open-course/peerReview/components/alerts/views/alerts"),r=require("pages/open-course/peerReview/components/submissionHeader/views/submissionHeader"),M=require("pages/open-course/peerReview/submissionTypes/getSubmissionTypeConfig"),s=require("pages/open-course/peerReview/viewModels/preview"),c=require("pages/open-course/peerReview/views/alerts/submitSuccess.graded.html"),m=require("pages/open-course/peerReview/views/alerts/submitSuccess.ungraded.html"),h=require("pages/open-course/peerReview/views/preview.html"),a=require("pages/open-course/peerReview/views/rubricQuestions"),b=require("pages/open-course/peerReview/views/submissionError.html"),w=require("pages/open-course/peerReview/views/submissionWarning.html"),g=require("bundles/verification/viewModels/verificationModule"),l=require("bundles/verification/views/verificationModule"),f=p.extend({name:"body",template:h,stateModelProperty:"viewModel",events:{'click [data-js="submit-button"]':"submit"},multitracker:{eventingVersion:2,namespace:"open_course_item.peer_review_my_project_preview",baseValues:["open_course_id","module_id","lesson_id","item_id"],definitions:{open_course_id:i.metadata("course.id"),module_id:i.metadata("lesson.module.id"),lesson_id:i.metadata("lesson.id"),item_id:i.metadata("id")},events:{render:[],"click.edit":'click [data-js~="edit-button"]',"click.submit":[]}},initialize:function initialize(i){_(this).bindAll("onSubmitSuccess","onSubmitFailure"),this.initializeOptions(i),this.isGraded=this.itemMetadata.isGradable(),this.isVerifiable=this.isGraded&&this.verificationDisplay.get("isProductVerificationEnabled"),this.initializeViewModels(),this.initializeEvents(),this.submissionTypeConfig=M(this.submissionSchema.typeName),this.editLink=e.join(this.itemMetadata.getCourseRelativeLink(),"submit"),this.showInlineReview=!0},initializeOptions:function initializeOptions(e){_(this).extend(_(e).pick("alerts","api","assignment","errorTree","itemMetadata","reviewSchema","submissionSchema","submission","verificationDisplay"))},initializeViewModels:function initializeViewModels(){this.viewModel=new s({},{alerts:this.alerts,api:this.api,errorTree:this.errorTree,itemMetadata:this.itemMetadata,submission:this.submission,submissionSchema:this.submissionSchema}),this.isVerifiable&&(this.verificationViewModel=new g({metadata:this.itemMetadata,verificationDisplay:this.verificationDisplay,canOptOut:!0}))},initializeEvents:function initializeEvents(){this.listenTo(this.viewModel,"change:state",this.updateInputs),this.listenTo(this,"view:appended",this.onAppendedView),this.isVerifiable&&this.listenTo(this.verificationViewModel,"verificationComplete",this.submit)},onAppendedView:function onAppendedView(){u.scroll(0)},renderSubviews:function renderSubviews(){this.region.append(r,{to:this.$$("submission-header"),initialize:{errorTree:this.errorTree,submission:this.submission},module:r}),this.region.append(this.submissionTypeConfig.ReviewView,{to:this.$$("review"),initialize:{submissionSchema:this.submissionSchema,submission:this.submission,errorTree:this.errorTree}}),this.region.append(o,{to:this.$$("submitting"),initialize:{text:"submitting"},module:o}),this.region.append(n,{to:this.$$("alerts"),initialize:{viewModel:this.alerts,errorPrefix:b(),warningPrefix:w()},module:n}),this.showInlineReview?(this.$$("rubric-questions-area").addClass("bt3-hide"),this.$$("display-area").removeClass("bt3-col-md-8 bt3-col-md-offset-0 bt3-col-md-pull-4 bt3-col-sm-10 bt3-col-sm-offset-1").addClass("bt3-col-md-12")):"closedPeer"!==this.itemMetadata.getTypeName()&&this.region.append(a,{to:this.$$("rubric-questions"),initialize:{itemMetadata:this.itemMetadata,schema:this.reviewSchema},module:a}),this.isVerifiable&&this.region.append(l,{to:this.$$("verification-container"),initialize:{verificationViewModel:this.verificationViewModel},module:l})},getVerifiableId:function getVerifiableId(){return this.verificationViewModel&&this.verificationViewModel.get("verifiableId")},postRender:function postRender(){this.track("render")},updateInputs:function updateInputs(){this.$(".bt3-btn").attr("disabled",this.viewModel.isState("submitting"))},submit:function submit(){this.viewModel.submit(this.getVerifiableId()).then(this.onSubmitSuccess,this.onSubmitFailure).done()},destroyVerificationViewModel:function destroyVerificationViewModel(){this.verificationViewModel&&this.verificationViewModel.trigger("destroy")},onSubmitSuccess:function onSubmitSuccess(r){this.track("click.submit",{status:"success"});var o=this.assignment.get("requiredReviewCount");this.destroyVerificationViewModel();var i=void 0;if("phasedPeer"===this.itemMetadata.getTypeName())i=e.join(this.itemMetadata.getCourseRelativeLink(),"submit");else{var n=this.isGraded?c:m,s=$(n({requiredReviewCount:o,pluralize:v}));d.push({type:"info",title:s.find('[data-js~="title"]').html(),text:s.find('[data-js~="text"]').html()}),i=e.join(this.itemMetadata.getCourseRelativeLink(),"give-feedback")}t.router.navigate(i,{replace:!0,trigger:!0})},onSubmitFailure:function onSubmitFailure(i){if(this.track("click.submit",{status:"error",error_info:(i||"").toString()}),i instanceof s.InvalidSubmissionException){var o=e.join(this.itemMetadata.getCourseRelativeLink(),"submit?submitError=1");t.router.navigate(o,{replace:!0,trigger:!0})}else if(i instanceof s.StaleAssignmentVersionException){var n=e.join(this.itemMetadata.getCourseRelativeLink(),"submit?showStaleAssignmentVersionError=1");t.router.navigate(n,{replace:!0,trigger:!0})}else if(!(i instanceof s.UnknownServerErrorException))throw i}});module.exports=f});
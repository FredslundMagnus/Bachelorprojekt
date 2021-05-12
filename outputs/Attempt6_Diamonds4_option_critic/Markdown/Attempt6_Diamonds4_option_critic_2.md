
# Parameters

    Name :                      Attempt6_Diamonds4_option_critic-2
    Main :                      option_critic_run
    Level :                     Levels.Causal7
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     72.0
    Batch :                     32
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      15050767488 function calls (14560193116 primitive calls) in 258900.90 seconds

##    Ordered by: cumulative time
   List reduced from 430 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.902 258900.902 {built-in method builtins.exec}
                      1    0.362    0.362 258900.902 258900.902 <string>:1(<module>)
                      1 1888.745 1888.745 258900.540 258900.540 optionCritic.py:195(option_critic_run)
                 549971    4.404    0.000 198141.181    0.360 tensor.py:195(backward)
                 549971    6.202    0.000 198136.688    0.360 __init__.py:68(backward)
                 549971 198117.938    0.360 198117.938    0.360 {method 'run_backward' of 'torch._C._EngineBase' objects}
        649167513/160380798 3087.206    0.000 37812.374    0.000 module.py:866(_call_impl)
               17599072 2638.503    0.000 36258.355    0.002 optionCritic.py:143(actor_loss_fn)
               54309635  274.604    0.000 35511.157    0.001 optionCritic.py:70(get_state)
               54309635  719.455    0.000 34478.877    0.001 container.py:117(forward)
              108619270  290.172    0.000 21963.990    0.000 conv.py:398(forward)
              108619270  155.788    0.000 21558.199    0.000 conv.py:390(_conv_forward)
              108619270 21402.411    0.000 21402.411    0.000 {built-in method conv2d}
              214690433  505.855    0.000 7610.136    0.000 linear.py:93(forward)
              214690433  198.126    0.000 6898.416    0.000 functional.py:1737(linear)
              214690433 6652.900    0.000 6652.900    0.000 {built-in method torch._C._nn.linear}
               17599072 1030.134    0.000 6155.911    0.000 optionCritic.py:91(get_action)
               17599072  384.119    0.000 4442.704    0.000 optionCritic.py:80(predict_option_termination)
                 549971   13.719    0.000 4122.835    0.007 optimizer.py:84(wrapper)
                 549971    7.351    0.000 4072.629    0.007 grad_mode.py:24(decorate_context)
                 549971   34.363    0.000 4052.073    0.007 adam.py:55(step)
                 549971  216.594    0.000 3981.356    0.007 _functional.py:53(adam)
               35198144  395.811    0.000 2484.307    0.000 distribution.py:34(__init__)
              162928905  173.685    0.000 2227.077    0.000 activation.py:713(forward)
              162928905  171.579    0.000 2053.392    0.000 functional.py:1364(leaky_relu)
               17599072  171.901    0.000 2038.823    0.000 categorical.py:115(log_prob)
                 137492   23.661    0.000 1935.554    0.014 optionCritic.py:116(critic_loss_fn)
              162928905 1848.419    0.000 1848.419    0.000 {built-in method torch._C._nn.leaky_relu}
               17599072  146.559    0.000 1776.516    0.000 bernoulli.py:34(__init__)
               17599072  231.493    0.000 1737.810    0.000 categorical.py:49(__init__)
               53136455  118.265    0.000 1691.315    0.000 optionCritic.py:77(get_Q)
               35335636  124.549    0.000 1355.572    0.000 optionCritic.py:88(get_terminations)
               17599072  710.547    0.000 1053.915    0.000 constraints.py:398(check)
                 549971    2.954    0.000  999.222    0.002 game.py:42(step)
                 549971    5.330    0.000  964.311    0.002 layers.py:827(step)
               15399176  882.439    0.000  882.439    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               17599072  140.731    0.000  823.060    0.000 distribution.py:240(_validate_sample)
                7699588  804.300    0.000  804.300    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               17599072  144.163    0.000  679.318    0.000 bernoulli.py:86(sample)
               17599072  669.302    0.000  669.302    0.000 constraints.py:364(check)
                7699588  665.376    0.000  665.376    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               54309635   68.116    0.000  637.761    0.000 activation.py:101(forward)
                 549971   26.443    0.000  606.427    0.001 layers.py:17(step)
               17599072   45.298    0.000  577.784    0.000 layer.py:106(move)
               17599072  297.970    0.000  570.445    0.000 categorical.py:123(entropy)
               54309635   63.154    0.000  569.646    0.000 functional.py:1195(relu)
              842269895  549.704    0.000  549.746    0.000 module.py:934(__getattr__)
               17599072  537.529    0.000  537.529    0.000 constraints.py:249(check)
              123193504  534.509    0.000  534.509    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               52797216   69.038    0.000  514.727    0.000 utils.py:106(__get__)
               54309635   50.641    0.000  499.231    0.000 flatten.py:39(forward)
               54309635  497.521    0.000  497.521    0.000 {built-in method relu}
               53072200   58.039    0.000  488.739    0.000 tensor.py:525(__rsub__)
                7699588  479.347    0.000  479.347    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               15399176  466.729    0.000  466.729    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                7699588  463.367    0.000  463.367    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               35198144  155.522    0.000  455.166    0.000 functional.py:46(broadcast_tensors)
               54309635  448.590    0.000  448.590    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               53072200  421.803    0.000  421.803    0.000 {built-in method rsub}
                6049681   14.469    0.000  413.602    0.000 tensor.py:575(__iter__)
               35335636  402.519    0.000  402.519    0.000 {method 'max' of 'torch._C._TensorBase' objects}
               17599072  109.963    0.000  401.054    0.000 categorical.py:108(sample)
              655217194  399.846    0.000  399.846    0.000 {built-in method torch._C._get_tracing_state}
               17599072   85.312    0.000  395.306    0.000 utils.py:11(broadcast_all)
               17599072   20.514    0.000  392.430    0.000 categorical.py:88(logits)
                6049681  390.280    0.000  390.280    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               52934708  383.844    0.000  383.844    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
               17599072   23.355    0.000  371.916    0.000 utils.py:82(probs_to_logits)
               52797216  358.893    0.000  358.893    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 549972   49.622    0.000  349.918    0.001 layers.py:793(update)
             2804720779  342.962    0.000  346.873    0.000 {built-in method builtins.len}
               17599072   77.074    0.000  344.065    0.000 layers.py:844(check)
                 137492  254.893    0.002  309.342    0.002 replaybuffer.py:42(sample_option_critic)
               52797216  306.782    0.000  306.782    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             2650979687  291.212    0.000  291.212    0.000 {method 'values' of 'collections.OrderedDict' objects}
               17599072  275.091    0.000  275.091    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               35198144  252.453    0.000  252.453    0.000 {built-in method broadcast_tensors}
                 549971   25.223    0.000  229.429    0.000 replaybuffer.py:34(save_option_critic)
               17599072   43.202    0.000  218.116    0.000 utils.py:77(clamp_probs)
               17599072  203.037    0.000  203.037    0.000 {built-in method bernoulli}
               53209692  197.936    0.000  197.936    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               17599072  175.004    0.000  175.004    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
               17599072  174.914    0.000  174.914    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
               17663327  166.351    0.000  166.351    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              105869416  158.668    0.000  158.668    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 549971   25.419    0.000  157.414    0.000 optimizer.py:189(zero_grad)
               17599072   32.158    0.000  150.846    0.000 layers.py:838(isFree)
               35198144  150.754    0.000  150.754    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               17599072  144.133    0.000  144.133    0.000 {built-in method clamp}
              231624025   86.015    0.000  131.171    0.000 {built-in method builtins.isinstance}
               17599072  130.445    0.000  130.445    0.000 {built-in method log}
               52862600  127.630    0.000  127.630    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               17599072  126.008    0.000  126.008    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
                3849804   73.654    0.000  123.915    0.000 layer.py:175(NoRock_update)
              109962404  100.558    0.000  118.688    0.000 layer.py:103(isFree)
               54309649  115.073    0.000  115.073    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               17599072  114.164    0.000  114.164    0.000 {built-in method all}
                3712306  111.153    0.000  111.153    0.000 {built-in method tensor}
               52797248   38.861    0.000  110.544    0.000 {built-in method builtins.all}
               17599072  103.189    0.000  103.189    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624158: <Attempt6_Diamonds4_option_critic_2> in cluster <dcc> Done

Job <Attempt6_Diamonds4_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:22:27 2021
Job was executed on host(s) <n-62-11-63>, in queue <hpc>, as user <s183914> in cluster <dcc> at Sun May  9 01:22:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun May  9 01:22:28 2021
Terminated at Wed May 12 01:17:36 2021
Results reported at Wed May 12 01:17:36 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   258265.20 sec.
    Max Memory :                                 867 MB
    Average Memory :                             859.51 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15517.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258957 sec.
    Turnaround time :                            258909 sec.

The output (if any) is above this job summary.


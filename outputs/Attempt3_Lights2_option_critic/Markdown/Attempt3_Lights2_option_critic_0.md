[W NNPACK.cpp:80] Could not initialize NNPACK! Reason: Unsupported hardware.

# Parameters

    Name :                      Attempt3_Lights2_option_critic-0
    Main :                      option_critic_run
    Level :                     Levels.Causal4
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     72.0
    Batch :                     25
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
    Minutes used :              4315 minutes.
    Hours used :                71 hours.

# Profiling


      30924532533 function calls (29966961206 primitive calls) in 258900.81 seconds

##    Ordered by: cumulative time
   List reduced from 439 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 258900.808 258900.808 {built-in method builtins.exec}
                      1    0.323    0.323 258900.808 258900.808 <string>:1(<module>)
                      1 3387.009 3387.009 258900.485 258900.485 optionCritic.py:195(option_critic_run)
        1270812921/313331451 9277.904    0.000 112999.989    0.000 module.py:866(_call_impl)
               34407125 8957.624    0.000 110632.387    0.003 optionCritic.py:143(actor_loss_fn)
              106386830  710.734    0.000 104615.947    0.001 optionCritic.py:70(get_state)
              106386830 2537.354    0.000 101771.160    0.001 container.py:117(forward)
              212773660  846.992    0.000 67329.026    0.000 conv.py:398(forward)
              212773660  372.549    0.000 66185.848    0.000 conv.py:390(_conv_forward)
              212773660 65813.299    0.000 65813.299    0.000 {built-in method conv2d}
                1376285   10.299    0.000 63142.865    0.046 tensor.py:195(backward)
                1376285   12.358    0.000 63132.279    0.046 __init__.py:68(backward)
                1376285 63085.435    0.046 63085.435    0.046 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1376285   29.907    0.000 27740.799    0.020 optimizer.py:84(wrapper)
                1376285   16.398    0.000 27620.031    0.020 grad_mode.py:24(decorate_context)
                1376285   93.921    0.000 27573.113    0.020 rmsprop.py:56(step)
                1376285  149.325    0.000 27371.012    0.020 _functional.py:203(rmsprop)
               19267972 24332.497    0.001 24332.497    0.001 {method 'sqrt' of 'torch._C._TensorBase' objects}
               34407125 3503.060    0.000 20880.345    0.001 optionCritic.py:91(get_action)
              419718281 1477.479    0.000 19516.120    0.000 linear.py:93(forward)
              419718281  517.838    0.000 17477.752    0.000 functional.py:1737(linear)
              419718281 16853.507    0.000 16853.507    0.000 {built-in method torch._C._nn.linear}
               34407125 1088.070    0.000 11743.670    0.000 optionCritic.py:80(predict_option_termination)
               68814250  966.617    0.000 7580.591    0.000 distribution.py:34(__init__)
              319160490  395.077    0.000 7287.746    0.000 activation.py:713(forward)
              319160490  387.645    0.000 6892.669    0.000 functional.py:1364(leaky_relu)
               34407125  565.769    0.000 6862.560    0.000 categorical.py:115(log_prob)
              319160490 6427.477    0.000 6427.477    0.000 {built-in method torch._C._nn.leaky_relu}
               34407125  803.903    0.000 6130.423    0.000 categorical.py:49(__init__)
              103585618  431.247    0.000 5813.762    0.000 optionCritic.py:77(get_Q)
               68951878  414.957    0.000 4770.272    0.000 optionCritic.py:88(get_terminations)
               34407125  261.484    0.000 4126.516    0.000 bernoulli.py:34(__init__)
               34407125 2515.346    0.000 3819.167    0.000 constraints.py:398(check)
                1376285    8.795    0.000 3334.827    0.002 game.py:42(step)
                 137628   31.183    0.000 3242.060    0.024 optionCritic.py:116(critic_loss_fn)
                1376285   13.905    0.000 3223.125    0.002 layers.py:827(step)
               34407125  432.101    0.000 2846.174    0.000 distribution.py:240(_validate_sample)
                1376285   60.475    0.000 2155.216    0.002 layers.py:17(step)
               34407125  177.598    0.000 2089.888    0.000 layer.py:106(move)
              106386830  147.242    0.000 2082.152    0.000 activation.py:101(forward)
               34407125  985.215    0.000 2042.077    0.000 categorical.py:123(entropy)
              106386830  130.894    0.000 1934.910    0.000 functional.py:1195(relu)
               34407125 1894.195    0.000 1894.195    0.000 constraints.py:249(check)
               19267972 1856.711    0.000 1856.711    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               34407125 1828.324    0.000 1828.324    0.000 constraints.py:364(check)
              106386830 1780.181    0.000 1780.181    0.000 {built-in method relu}
             1285952056 1738.787    0.000 1738.787    0.000 {built-in method torch._C._get_tracing_state}
              103221375  194.157    0.000 1707.089    0.000 utils.py:106(__get__)
              240849875 1582.314    0.000 1582.314    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               34407125  285.247    0.000 1574.131    0.000 bernoulli.py:86(sample)
              103496631  158.777    0.000 1494.400    0.000 tensor.py:525(__rsub__)
              103221375 1455.164    0.000 1455.164    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
             1647133218 1453.662    0.000 1453.664    0.000 module.py:934(__getattr__)
              106386830  102.725    0.000 1426.796    0.000 flatten.py:39(forward)
               34407125  263.396    0.000 1369.940    0.000 layers.py:844(check)
               34407125   68.553    0.000 1357.442    0.000 categorical.py:88(logits)
              103359003 1331.013    0.000 1331.013    0.000 {method 'sigmoid' of 'torch._C._TensorBase' objects}
              106386830 1324.072    0.000 1324.072    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              103496631 1305.774    0.000 1305.774    0.000 {built-in method rsub}
               34407125  331.439    0.000 1299.544    0.000 categorical.py:108(sample)
               34407125   68.146    0.000 1288.889    0.000 utils.py:82(probs_to_logits)
               68814250  359.422    0.000 1137.246    0.000 functional.py:46(broadcast_tensors)
               68951878 1105.594    0.000 1105.594    0.000 {method 'max' of 'torch._C._TensorBase' objects}
                1376286  144.562    0.000 1048.077    0.001 layers.py:793(update)
              103221375  997.153    0.000  997.153    0.000 {method 'all' of 'torch._C._TensorBase' objects}
             5602563475  970.034    0.000  981.693    0.000 {built-in method builtins.len}
               15139135   40.615    0.000  948.523    0.000 tensor.py:575(__iter__)
               15139135  876.015    0.000  876.015    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               34407125  123.692    0.000  801.959    0.000 utils.py:77(clamp_probs)
               34407125  156.879    0.000  801.772    0.000 utils.py:11(broadcast_all)
             5189638514  788.173    0.000  788.173    0.000 {method 'values' of 'collections.OrderedDict' objects}
               34407125  747.101    0.000  747.101    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}
               68814250  680.858    0.000  680.858    0.000 {built-in method broadcast_tensors}
               34407125  678.267    0.000  678.267    0.000 {method 'clamp' of 'torch._C._TensorBase' objects}
                1376285   69.809    0.000  668.322    0.000 replaybuffer.py:34(save_option_critic)
              103634259  651.849    0.000  651.849    0.000 {method 'squeeze' of 'torch._C._TensorBase' objects}
               34407125  629.529    0.000  629.529    0.000 {method 'gather' of 'torch._C._TensorBase' objects}
              206718006  592.908    0.000  592.908    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               34407125  576.983    0.000  576.983    0.000 {built-in method clamp}
               68814250  535.957    0.000  535.957    0.000 {method 'reshape' of 'torch._C._TensorBase' objects}
               34496112  521.556    0.000  521.556    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               34407125  511.982    0.000  511.982    0.000 {built-in method bernoulli}
                1376285   86.967    0.000  449.671    0.000 optimizer.py:189(zero_grad)
               34407125  440.200    0.000  440.200    0.000 {built-in method all}
               34407125   92.125    0.000  436.373    0.000 layers.py:838(isFree)
               13762860  264.044    0.000  422.497    0.000 layer.py:159(update)
               34407125  418.784    0.000  418.784    0.000 {built-in method log}
               34407125  413.573    0.000  413.573    0.000 {method 'abs' of 'torch._C._TensorBase' objects}
               19267972  371.205    0.000  371.205    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               19267972  360.069    0.000  360.069    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              276900052  281.504    0.000  344.247    0.000 layer.py:103(isFree)
               34407125  309.336    0.000  309.336    0.000 {built-in method multinomial}
               19267972  301.204    0.000  301.204    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              103221400   76.289    0.000  293.209    0.000 {built-in method builtins.all}
                8670598  288.391    0.000  288.391    0.000 {built-in method tensor}
              106386844  284.347    0.000  284.347    0.000 {method 'to' of 'torch._C._TensorBase' objects}
              453448312  185.068    0.000  282.306    0.000 {built-in method builtins.isinstance}
              103313138  271.474    0.000  271.474    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               34407125  267.624    0.000  267.624    0.000 {method 'expand' of 'torch._C._TensorBase' objects}
                 137628  191.114    0.001  253.010    0.002 replaybuffer.py:42(sample_option_critic)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9607840: <Attempt3_Lights2_option_critic_0> in cluster <dcc> Done

Job <Attempt3_Lights2_option_critic_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 13:31:22 2021
Job was executed on host(s) <n-62-23-27>, in queue <hpc>, as user <s183914> in cluster <dcc> at Mon May  3 13:31:23 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon May  3 13:31:23 2021
Terminated at Thu May  6 13:26:33 2021
Results reported at Thu May  6 13:26:33 2021

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

    CPU time :                                   258894.78 sec.
    Max Memory :                                 1035 MB
    Average Memory :                             1016.60 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               15349.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   258975 sec.
    Turnaround time :                            258911 sec.

The output (if any) is above this job summary.


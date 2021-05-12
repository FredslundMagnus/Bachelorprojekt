
# Parameters

    Name :                      Causal3_Conver4_3counterfactsNOCRASH-1
    Main :                      CFagent
    Level :                     Levels.Causal3
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
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
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      55776590479 function calls (55428672240 primitive calls) in 86113.58 seconds

##    Ordered by: cumulative time
   List reduced from 509 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86113.579 86113.579 {built-in method builtins.exec}
                      1    4.156    4.156 86113.579 86113.579 <string>:1(<module>)
                      1  294.656  294.656 86109.423 86109.423 main.py:80(CFagent)
                8110191   29.918    0.000 24376.334    0.003 agent.py:29(learn)
                2703397 2563.866    0.001 22882.617    0.008 agent.py:212(counterfact)
                8110190  616.530    0.000 20338.460    0.003 learner.py:42(Qlearn)
        385920916/38004368 1538.649    0.000 13982.876    0.000 module.py:866(_call_impl)
               29894178   82.577    0.000 13266.150    0.000 network.py:28(forward)
               29894178  413.403    0.000 12994.503    0.000 container.py:117(forward)
                2703397   12.581    0.000 12808.837    0.005 game.py:42(step)
                2703397   15.926    0.000 12190.234    0.005 layers.py:827(step)
                2703397  279.117    0.000 9409.349    0.003 agent.py:54(_learn)
               93591050 8728.263    0.000 8728.263    0.000 {built-in method tensor}
                2703397  276.264    0.000 8707.166    0.003 agent.py:204(_learn)
                8110190   70.521    0.000 8644.515    0.001 optimizer.py:84(wrapper)
               87308883   52.876    0.000 8577.179    0.000 game.py:38(board)
                5486092  114.812    0.000 8455.141    0.002 agent.py:176(choose_action)
                8110190   33.882    0.000 8316.934    0.001 grad_mode.py:24(decorate_context)
                8110190  239.192    0.000 8208.295    0.001 adam.py:55(step)
               10891103  282.278    0.000 7780.515    0.001 agent.py:49(__call__)
                8110190 1674.521    0.000 7709.933    0.001 _functional.py:53(adam)
                2703397  228.707    0.000 7636.690    0.003 layers.py:17(step)
              269889356  413.095    0.000 7381.574    0.000 layer.py:106(move)
                2703397   81.794    0.000 6212.677    0.002 agent.py:117(_learn)
                2703397 3025.208    0.001 5669.753    0.002 replaybuffer.py:28(teleporter_save_data)
                8110190   33.973    0.000 5058.749    0.001 tensor.py:195(backward)
                8110190   31.547    0.000 5023.537    0.001 __init__.py:68(backward)
                8110190 4810.899    0.001 4810.899    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2703397 2831.723    0.001 4764.525    0.002 agent.py:88(interveen)
                2703397 3805.449    0.001 4684.748    0.002 replaybuffer.py:22(sample_data)
               59788356  129.092    0.000 4676.574    0.000 conv.py:398(forward)
                2703397 3694.455    0.001 4547.494    0.002 replaybuffer.py:67(sample_data)
                2703398  372.118    0.000 4516.993    0.002 layers.py:793(update)
               59788356   78.041    0.000 4491.693    0.000 conv.py:390(_conv_forward)
               59788356 4413.652    0.000 4413.652    0.000 {built-in method conv2d}
               86508696 2388.570    0.000 4413.297    0.000 layer.py:175(NoRock_update)
              269889356  935.342    0.000 4352.484    0.000 layers.py:844(check)
               84275740  167.280    0.000 3772.386    0.000 linear.py:93(forward)
               84275740   68.299    0.000 3527.706    0.000 functional.py:1737(linear)
               84275740 3443.112    0.000 3443.112    0.000 {built-in method torch._C._nn.linear}
              189809579 2442.479    0.000 2442.479    0.000 {built-in method clone}
                2703397 1592.966    0.001 2380.813    0.001 agent.py:67(modify)
              269889356  422.188    0.000 2233.866    0.000 layers.py:838(isFree)
              114169918   88.074    0.000 2117.163    0.000 activation.py:713(forward)
              114169918   94.812    0.000 2029.090    0.000 functional.py:1364(leaky_relu)
               13594500   92.604    0.000 1962.676    0.000 agent.py:59(modify_board)
              114169918 1915.440    0.000 1915.440    0.000 {built-in method torch._C._nn.leaky_relu}
             2014265931 1517.703    0.000 1811.678    0.000 layer.py:103(isFree)
                5486092 1521.629    0.000 1778.805    0.000 agent.py:187(convert_values)
               40628465 1655.405    0.000 1655.405    0.000 {built-in method cat}
              151390212 1596.450    0.000 1596.450    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2703397 1069.627    0.000 1424.704    0.001 replaybuffer.py:73(CF_save_data)
              151390212 1387.476    0.000 1387.476    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2703396   47.266    0.000 1354.410    0.001 agent.py:172(__call__)
                2703397   47.437    0.000 1283.563    0.000 agent.py:112(__call__)
               13594500 1250.946    0.000 1250.946    0.000 {built-in method torch._C._nn.one_hot}
                3844898   41.399    0.000 1236.580    0.000 layers.py:849(restart)
                8110190  196.974    0.000 1195.098    0.000 optimizer.py:189(zero_grad)
             1070603957 1082.182    0.000 1082.182    0.000 layer.py:154(elements)
             4132298304  707.279    0.000 1015.526    0.000 enum.py:646(__hash__)
              274605092  222.276    0.000  960.310    0.000 {built-in method builtins.any}
              269889356  582.164    0.000  923.440    0.000 layers.py:246(check)
                3844898   18.892    0.000  893.079    0.000 level.py:8(__init__)
               75695106  857.782    0.000  857.782    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              269889356  495.909    0.000  835.909    0.000 layers.py:286(check)
               10891103  294.229    0.000  808.519    0.000 exploration.py:53(softmaxer)
               75695106  740.195    0.000  740.195    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
        10900888305/10900888302  661.723    0.000  738.175    0.000 {built-in method builtins.len}
             2398454118  605.656    0.000  738.034    0.000 layers.py:809(<genexpr>)
               75695106  720.193    0.000  720.193    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               75695106  712.109    0.000  712.109    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                3844898   77.112    0.000  696.893    0.000 levels.py:164(generate)
                2703397   53.273    0.000  688.876    0.000 replaybuffer.py:18(stacker)
                2703396   52.308    0.000  668.945    0.000 replaybuffer.py:63(stacker)
              206107475  639.002    0.000  639.002    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              270339800   72.791    0.000  595.338    0.000 {built-in method builtins.all}
                2703397  336.163    0.000  557.601    0.000 collector.py:46(collect)
              825059779  200.860    0.000  553.553    0.000 layers.py:799(<genexpr>)
               75695106  548.722    0.000  548.722    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7689796   71.006    0.000  518.711    0.000 level.py:41(notUsed)
             5096217554  459.901    0.000  459.901    0.000 layer.py:99(positions)
               13096590  167.316    0.000  435.723    0.000 random.py:315(sample)
              529865826  344.640    0.000  428.432    0.000 tensor.py:906(grad)
              269889356  264.886    0.000  420.311    0.000 layers.py:313(check)
              269889356  251.319    0.000  397.821    0.000 layers.py:273(check)
                8110190   11.215    0.000  395.330    0.000 loss.py:527(forward)
                8110190   30.179    0.000  384.114    0.000 functional.py:2898(mse_loss)
              269889356  242.157    0.000  360.321    0.000 layers.py:48(check)
               59788356   41.283    0.000  345.025    0.000 flatten.py:39(forward)
             4132329247  308.253    0.000  308.253    0.000 {built-in method builtins.hash}
               23189615  306.438    0.000  306.438    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               59788356  303.742    0.000  303.742    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               30759184   36.238    0.000  292.240    0.000 layer.py:77(restart)
               86508696  289.584    0.000  289.584    0.000 layer.py:186(<listcomp>)
              269889356  180.320    0.000  273.217    0.000 layers.py:23(check)
              396815980  271.931    0.000  271.931    0.000 {built-in method torch._C._get_tracing_state}
               10891103  259.049    0.000  259.049    0.000 {built-in method multinomial}
                8110190  252.163    0.000  252.163    0.000 {built-in method torch._C._nn.mse_loss}
               86508696  248.349    0.000  248.349    0.000 layer.py:187(<listcomp>)
               13596282   21.418    0.000  242.705    0.000 tensor.py:525(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624188: <Causal3_Conver4_3counterfactsNOCRASH_1> in cluster <dcc> Done

Job <Causal3_Conver4_3counterfactsNOCRASH_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
Job was executed on host(s) <n-62-20-6>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue May 11 03:10:48 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May 11 03:10:48 2021
Terminated at Wed May 12 03:06:09 2021
Results reported at Wed May 12 03:06:09 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85900.79 sec.
    Max Memory :                                 8168 MB
    Average Memory :                             5695.85 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8216.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86121 sec.
    Turnaround time :                            265012 sec.

The output (if any) is above this job summary.

Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 71, in __init__
    cProfile.run(
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.4/lib/python3.8/profile.py", line 53, in run
    prof.run(statement)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 2, in <module>
  File "main.py", line 85, in CFagent
    CFagent = CFAgent(env, **defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/agent.py", line 171, in __init__
    if a != b:
NameError: name 'a' is not defined


# Parameters

    Name :                      Causal3_Conver4_3counterfactsNOCRASH-1
    Main :                      CFagent
    Level :                     Levels.Causal3
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     24.0
    Batch :                     100
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
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      158561 function calls (158272 primitive calls) in 5.53 seconds

##    Ordered by: cumulative time
   List reduced from 207 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    5.526    5.526 {built-in method builtins.exec}
                      1    0.000    0.000    5.526    5.526 <string>:1(<module>)
                      1    0.000    0.000    5.526    5.526 main.py:80(CFagent)
                      3    0.000    0.000    5.469    1.823 agent.py:16(__init__)
                      3    0.000    0.000    5.468    1.823 network.py:37(__init__)
                      1    0.000    0.000    5.452    5.452 agent.py:109(__init__)
                      9    0.000    0.000    5.417    0.602 module.py:573(to)
                  111/9    0.001    0.000    5.417    0.602 module.py:385(_apply)
                     84    0.000    0.000    5.415    0.064 module.py:667(convert)
                     84    5.411    0.064    5.415    0.064 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.054    0.054 game.py:9(__init__)
                      9    0.000    0.000    0.051    0.006 network.py:17(__init__)
                     18    0.000    0.000    0.041    0.002 conv.py:370(__init__)
                     18    0.007    0.000    0.041    0.002 conv.py:66(__init__)
                     42    0.000    0.000    0.037    0.001 init.py:347(kaiming_uniform_)
                      1    0.000    0.000    0.036    0.036 layers.py:793(update)
                     84    0.035    0.000    0.035    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                     18    0.000    0.000    0.032    0.002 conv.py:114(reset_parameters)
                    100    0.001    0.000    0.032    0.000 layers.py:849(restart)
                    100    0.000    0.000    0.023    0.000 level.py:8(__init__)
                    100    0.002    0.000    0.019    0.000 levels.py:164(generate)
                    200    0.002    0.000    0.015    0.000 level.py:41(notUsed)
                    200    0.005    0.000    0.011    0.000 layers.py:36(reset)
                      1    0.000    0.000    0.010    0.010 layers.py:751(__init__)
                      7    0.000    0.000    0.009    0.001 layers.py:782(add)
                      1    0.000    0.000    0.009    0.009 agent.py:158(__init__)
                      1    0.000    0.000    0.008    0.008 agent.py:39(__init__)
                    800    0.001    0.000    0.008    0.000 layer.py:77(restart)
                      8    0.001    0.000    0.008    0.001 layer.py:61(__init__)
                     24    0.000    0.000    0.007    0.000 linear.py:75(__init__)
                    200    0.000    0.000    0.006    0.000 level.py:38(elementsIn)
                     24    0.000    0.000    0.006    0.000 linear.py:86(reset_parameters)
                      1    0.000    0.000    0.006    0.006 game.py:30(<setcomp>)
                     41    0.002    0.000    0.005    0.000 game.py:30(<listcomp>)
                   6575    0.005    0.000    0.005    0.000 level.py:32(inverse)
                  17196    0.003    0.000    0.004    0.000 enum.py:646(__hash__)
                   8335    0.003    0.000    0.004    0.000 layer.py:138(add)
                    200    0.002    0.000    0.004    0.000 level.py:39(<listcomp>)
                   1698    0.002    0.000    0.004    0.000 module.py:950(__setattr__)
                  15022    0.004    0.000    0.004    0.000 enum.py:352(<genexpr>)
                    100    0.001    0.000    0.003    0.000 level.py:16(<dictcomp>)
                    4/1    0.000    0.000    0.003    0.003 __init__.py:144(_lazy_init)
                      8    0.002    0.000    0.003    0.000 layer.py:175(NoRock_update)
                    114    0.001    0.000    0.003    0.000 module.py:250(__init__)
                      1    0.003    0.003    0.003    0.003 {built-in method torch._C._cuda_init}
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                  17056    0.003    0.000    0.003    0.000 layer.py:190(grid)
                     84    0.002    0.000    0.002    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                    200    0.001    0.000    0.002    0.000 {built-in method _functools.reduce}
                   2360    0.001    0.000    0.002    0.000 types.py:171(__get__)
                     42    0.000    0.000    0.002    0.000 init.py:337(_calculate_correct_fan)
                    200    0.001    0.000    0.002    0.000 random.py:315(sample)
                  17196    0.001    0.000    0.001    0.000 {built-in method builtins.hash}
                  18960    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
                     33    0.000    0.000    0.001    0.000 activation.py:708(__init__)
                   4805    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
                    800    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                      7    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                   8351    0.001    0.000    0.001    0.000 layer.py:154(elements)
                   8400    0.001    0.000    0.001    0.000 level.py:39(<lambda>)
                    213    0.000    0.000    0.001    0.000 module.py:1338(children)
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                    213    0.001    0.000    0.001    0.000 module.py:1347(named_children)
                    834    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
                     18    0.000    0.000    0.001    0.000 flatten.py:34(__init__)
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                   1799    0.001    0.000    0.001    0.000 {method 'split' of 'str' objects}
                    900    0.000    0.000    0.001    0.000 layers.py:799(<genexpr>)
                    272    0.000    0.000    0.001    0.000 {built-in method builtins.hasattr}
                   2359    0.001    0.000    0.001    0.000 enum.py:659(name)
                     84    0.000    0.000    0.000    0.000 module.py:322(register_parameter)
                      8    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                     42    0.000    0.000    0.000    0.000 init.py:112(uniform_)
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                   4917    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                    490    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                    800    0.000    0.000    0.000    0.000 layer.py:142(clear)
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                      1    0.000    0.000    0.000    0.000 agent.py:167(<listcomp>)
                    490    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
                     84    0.000    0.000    0.000    0.000 parameter.py:23(__new__)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:114(__init__)
                      1    0.000    0.000    0.000    0.000 layers.py:266(__init__)
                     84    0.000    0.000    0.000    0.000 module.py:389(compute_should_use_set_data)
                      1    0.000    0.000    0.000    0.000 layers.py:306(__init__)
                     31    0.000    0.000    0.000    0.000 module.py:1240(parameters)
                     31    0.000    0.000    0.000    0.000 module.py:1264(named_parameters)
                      2    0.000    0.000    0.000    0.000 {built-in method zeros}
                   1422    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
                     84    0.000    0.000    0.000    0.000 {built-in method _make_subclass}
                     31    0.000    0.000    0.000    0.000 module.py:1227(_named_members)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632729: <Causal3_Conver4_3counterfactsNOCRASH_1> in cluster <dcc> Done

Job <Causal3_Conver4_3counterfactsNOCRASH_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:11:09 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:13:14 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:13:14 2021
Terminated at Wed May 12 15:13:26 2021
Results reported at Wed May 12 15:13:26 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   5.28 sec.
    Max Memory :                                 4 MB
    Average Memory :                             4.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16380.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                5
    Run time :                                   13 sec.
    Turnaround time :                            3737 sec.

The output (if any) is above this job summary.

Traceback (most recent call last):
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 71, in __init__
    cProfile.run(
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.4/lib/python3.8/profile.py", line 53, in run
    prof.run(statement)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 2, in <module>
  File "main.py", line 85, in CFagent
    CFagent = CFAgent(env, **defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/agent.py", line 171, in __init__
    if a != b:
NameError: name 'a' is not defined


# Parameters

    Name :                      Causal3_Conver4_3counterfactsNOCRASH-1
    Main :                      CFagent
    Level :                     Levels.Causal3
    Failed actions chance :     0
    Use model :                 True
    Depth :                     3
    Model explore :             1000000
    Samples :                   5
    Hours :                     0.0
    Batch :                     100
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
    Cf convert :                4
    Counterfacts :              3
    Topn :                      5
    Random counterfacts :       False
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              0 minutes.
    Hours used :                0 hours.

# Profiling


      158699 function calls (158410 primitive calls) in 3.74 seconds

##    Ordered by: cumulative time
   List reduced from 207 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000    3.735    3.735 {built-in method builtins.exec}
                      1    0.000    0.000    3.735    3.735 <string>:1(<module>)
                      1    0.000    0.000    3.735    3.735 main.py:80(CFagent)
                      3    0.000    0.000    3.683    1.228 agent.py:16(__init__)
                      3    0.000    0.000    3.682    1.227 network.py:37(__init__)
                      1    0.000    0.000    3.666    3.666 agent.py:109(__init__)
                      9    0.000    0.000    3.636    0.404 module.py:573(to)
                  111/9    0.001    0.000    3.636    0.404 module.py:385(_apply)
                     84    0.000    0.000    3.634    0.043 module.py:667(convert)
                     84    3.608    0.043    3.634    0.043 {method 'to' of 'torch._C._TensorBase' objects}
                      1    0.002    0.002    0.049    0.049 game.py:9(__init__)
                      9    0.000    0.000    0.046    0.005 network.py:17(__init__)
                      1    0.000    0.000    0.037    0.037 layers.py:793(update)
                     18    0.000    0.000    0.036    0.002 conv.py:370(__init__)
                     18    0.007    0.000    0.035    0.002 conv.py:66(__init__)
                    100    0.001    0.000    0.033    0.000 layers.py:849(restart)
                    4/1    0.000    0.000    0.026    0.026 __init__.py:144(_lazy_init)
                      1    0.026    0.026    0.026    0.026 {built-in method torch._C._cuda_init}
                    100    0.000    0.000    0.023    0.000 level.py:8(__init__)
                    100    0.003    0.000    0.020    0.000 levels.py:164(generate)
                    200    0.002    0.000    0.014    0.000 level.py:41(notUsed)
                     18    0.006    0.000    0.014    0.001 conv.py:114(reset_parameters)
                     84    0.000    0.000    0.014    0.000 parameter.py:23(__new__)
                     84    0.014    0.000    0.014    0.000 {built-in method _make_subclass}
                     42    0.000    0.000    0.012    0.000 init.py:347(kaiming_uniform_)
                    200    0.005    0.000    0.010    0.000 layers.py:36(reset)
                      1    0.000    0.000    0.009    0.009 agent.py:158(__init__)
                     84    0.009    0.000    0.009    0.000 {method 'uniform_' of 'torch._C._TensorBase' objects}
                      1    0.000    0.000    0.009    0.009 agent.py:39(__init__)
                    800    0.001    0.000    0.008    0.000 layer.py:77(restart)
                      1    0.000    0.000    0.008    0.008 layers.py:751(__init__)
                      7    0.000    0.000    0.007    0.001 layers.py:782(add)
                     24    0.000    0.000    0.007    0.000 linear.py:75(__init__)
                      8    0.000    0.000    0.007    0.001 layer.py:61(__init__)
                    200    0.000    0.000    0.006    0.000 level.py:38(elementsIn)
                     24    0.000    0.000    0.006    0.000 linear.py:86(reset_parameters)
                   6533    0.005    0.000    0.005    0.000 level.py:32(inverse)
                  17211    0.003    0.000    0.004    0.000 enum.py:646(__hash__)
                   8350    0.003    0.000    0.004    0.000 layer.py:138(add)
                    200    0.002    0.000    0.004    0.000 level.py:39(<listcomp>)
                   1698    0.002    0.000    0.004    0.000 module.py:950(__setattr__)
                      8    0.002    0.000    0.003    0.000 layer.py:175(NoRock_update)
                    100    0.001    0.000    0.003    0.000 level.py:16(<dictcomp>)
                     84    0.003    0.000    0.003    0.000 init.py:268(_calculate_fan_in_and_fan_out)
                    114    0.001    0.000    0.003    0.000 module.py:250(__init__)
                     42    0.000    0.000    0.003    0.000 init.py:337(_calculate_correct_fan)
                  15022    0.003    0.000    0.003    0.000 enum.py:352(<genexpr>)
                      1    0.000    0.000    0.003    0.003 replaybuffer.py:8(__init__)
                      1    0.003    0.003    0.003    0.003 replaybuffer.py:11(<listcomp>)
                  17056    0.002    0.000    0.002    0.000 layer.py:190(grid)
                      1    0.000    0.000    0.002    0.002 game.py:30(<setcomp>)
                     41    0.001    0.000    0.002    0.000 game.py:30(<listcomp>)
                    200    0.001    0.000    0.002    0.000 {built-in method _functools.reduce}
                    200    0.001    0.000    0.002    0.000 random.py:315(sample)
                  17211    0.001    0.000    0.001    0.000 {built-in method builtins.hash}
                  19005    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
                     33    0.000    0.000    0.001    0.000 activation.py:708(__init__)
                   4805    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
                    800    0.001    0.000    0.001    0.000 layer.py:147(clear2)
                   2360    0.001    0.000    0.001    0.000 types.py:171(__get__)
                   8366    0.001    0.000    0.001    0.000 layer.py:154(elements)
                    213    0.000    0.000    0.001    0.000 module.py:1338(children)
                   8400    0.001    0.000    0.001    0.000 level.py:39(<lambda>)
                      9    0.000    0.000    0.001    0.000 container.py:62(__init__)
                    213    0.001    0.000    0.001    0.000 module.py:1347(named_children)
                      7    0.000    0.000    0.001    0.000 inspect.py:325(getmembers)
                    844    0.000    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
                    100    0.000    0.000    0.001    0.000 {built-in method builtins.all}
                      3    0.000    0.000    0.001    0.000 learner.py:16(__init__)
                    210    0.001    0.000    0.001    0.000 {built-in method math.sqrt}
                     18    0.000    0.000    0.001    0.000 flatten.py:34(__init__)
                    272    0.000    0.000    0.001    0.000 {built-in method builtins.hasattr}
                    900    0.000    0.000    0.001    0.000 layers.py:799(<genexpr>)
                     84    0.000    0.000    0.000    0.000 module.py:322(register_parameter)
                      3    0.000    0.000    0.000    0.000 adam.py:34(__init__)
                      3    0.000    0.000    0.000    0.000 optimizer.py:34(__init__)
                    345    0.000    0.000    0.000    0.000 module.py:934(__getattr__)
                     42    0.000    0.000    0.000    0.000 init.py:112(uniform_)
                   4917    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
                    490    0.000    0.000    0.000    0.000 abc.py:96(__instancecheck__)
                     42    0.000    0.000    0.000    0.000 init.py:12(_no_grad_uniform_)
                     93    0.000    0.000    0.000    0.000 module.py:361(add_module)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:119(__enter__)
                    336    0.000    0.000    0.000    0.000 grad_mode.py:200(__init__)
                      8    0.000    0.000    0.000    0.000 layer.py:71(<listcomp>)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:123(__exit__)
                     90    0.000    0.000    0.000    0.000 utils.py:9(parse)
                      1    0.000    0.000    0.000    0.000 agent.py:167(<listcomp>)
                    490    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
                    800    0.000    0.000    0.000    0.000 layer.py:142(clear)
                   2359    0.000    0.000    0.000    0.000 enum.py:659(name)
                    168    0.000    0.000    0.000    0.000 grad_mode.py:114(__init__)
                     84    0.000    0.000    0.000    0.000 module.py:389(compute_should_use_set_data)
                     31    0.000    0.000    0.000    0.000 module.py:1240(parameters)
                      2    0.000    0.000    0.000    0.000 {built-in method zeros}
                   1799    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
                     31    0.000    0.000    0.000    0.000 module.py:1264(named_parameters)
                      1    0.000    0.000    0.000    0.000 layers.py:306(__init__)
                     31    0.000    0.000    0.000    0.000 module.py:1227(_named_members)
                    350    0.000    0.000    0.000    0.000 enum.py:351(__iter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9632772: <Causal3_Conver4_3counterfactsNOCRASH_1> in cluster <dcc> Done

Job <Causal3_Conver4_3counterfactsNOCRASH_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed May 12 14:13:39 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed May 12 15:14:40 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 12 15:14:40 2021
Terminated at Wed May 12 15:14:46 2021
Results reported at Wed May 12 15:14:46 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   4.82 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   7 sec.
    Turnaround time :                            3667 sec.

The output (if any) is above this job summary.


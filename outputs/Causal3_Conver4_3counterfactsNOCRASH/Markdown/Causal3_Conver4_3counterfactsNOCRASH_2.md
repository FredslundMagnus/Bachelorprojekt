
# Parameters

    Name :                      Causal3_Conver4_3counterfactsNOCRASH-2
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      55618430301 function calls (55272006542 primitive calls) in 86108.44 seconds

##    Ordered by: cumulative time
   List reduced from 509 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86108.436 86108.436 {built-in method builtins.exec}
                      1    4.163    4.163 86108.436 86108.436 <string>:1(<module>)
                      1  300.776  300.776 86104.273 86104.273 main.py:80(CFagent)
                8156910   28.340    0.000 24531.914    0.003 agent.py:29(learn)
                2718970 2458.329    0.001 22552.325    0.008 agent.py:212(counterfact)
                8156901  616.602    0.000 20452.965    0.003 learner.py:42(Qlearn)
        384353798/37931730 1509.382    0.000 13954.734    0.000 module.py:866(_call_impl)
               29774829   81.951    0.000 13243.678    0.000 network.py:28(forward)
               29774829  411.125    0.000 12981.231    0.000 container.py:117(forward)
                2718970   12.866    0.000 12668.164    0.005 game.py:42(step)
                2718970   17.632    0.000 12043.614    0.004 layers.py:827(step)
                2718970  291.836    0.000 9467.762    0.003 agent.py:54(_learn)
                2718970  289.334    0.000 8756.774    0.003 agent.py:204(_learn)
                8156901   70.232    0.000 8706.348    0.001 optimizer.py:84(wrapper)
               93207173 8685.995    0.000 8685.995    0.000 {built-in method tensor}
               86890491   53.122    0.000 8532.315    0.000 game.py:38(board)
                8156901   33.782    0.000 8372.033    0.001 grad_mode.py:24(decorate_context)
                5371888  109.833    0.000 8315.409    0.002 agent.py:176(choose_action)
                8156901  236.264    0.000 8257.965    0.001 adam.py:55(step)
                8156901 1688.559    0.000 7760.138    0.001 _functional.py:53(adam)
               10808109  285.988    0.000 7746.529    0.001 agent.py:49(__call__)
                2718970  225.314    0.000 7539.331    0.003 layers.py:17(step)
              271522144  417.556    0.000 7290.526    0.000 layer.py:106(move)
                2718970   83.253    0.000 6260.116    0.002 agent.py:117(_learn)
                2718970 3179.307    0.001 5891.584    0.002 replaybuffer.py:28(teleporter_save_data)
                8156901   32.372    0.000 5096.534    0.001 tensor.py:195(backward)
                8156901   30.098    0.000 5062.893    0.001 __init__.py:68(backward)
                2718970 2933.974    0.001 4888.644    0.002 agent.py:88(interveen)
                8156901 4851.067    0.001 4851.067    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2718970 3780.891    0.001 4691.926    0.002 replaybuffer.py:22(sample_data)
               59549658  131.345    0.000 4674.386    0.000 conv.py:398(forward)
                2718970 3648.109    0.001 4524.467    0.002 replaybuffer.py:67(sample_data)
               59549658   73.028    0.000 4486.972    0.000 conv.py:390(_conv_forward)
                2718971  381.222    0.000 4465.708    0.002 layers.py:793(update)
               87007032 2387.856    0.000 4422.340    0.000 layer.py:175(NoRock_update)
               59549658 4413.944    0.000 4413.944    0.000 {built-in method conv2d}
              271522144  919.936    0.000 4318.810    0.000 layers.py:844(check)
               83886547  159.803    0.000 3795.015    0.000 linear.py:93(forward)
               83886547   65.140    0.000 3556.195    0.000 functional.py:1737(linear)
               83886547 3474.540    0.000 3474.540    0.000 {built-in method torch._C._nn.linear}
              194072590 2494.680    0.000 2494.680    0.000 {built-in method clone}
                2718970 1603.140    0.001 2395.760    0.001 agent.py:67(modify)
              271522144  406.818    0.000 2183.119    0.000 layers.py:838(isFree)
              113661376   82.684    0.000 2108.401    0.000 activation.py:713(forward)
              113661376   90.036    0.000 2025.717    0.000 functional.py:1364(leaky_relu)
               13527079   94.811    0.000 1961.153    0.000 agent.py:59(modify_board)
              113661376 1915.856    0.000 1915.856    0.000 {built-in method torch._C._nn.leaky_relu}
             1949233580 1487.792    0.000 1776.301    0.000 layer.py:103(isFree)
                5371888 1498.222    0.000 1750.538    0.000 agent.py:187(convert_values)
               40716734 1708.269    0.000 1708.269    0.000 {built-in method cat}
              152262140 1605.697    0.000 1605.697    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              152262140 1392.576    0.000 1392.576    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2718970 1042.320    0.000 1374.414    0.001 replaybuffer.py:73(CF_save_data)
                2718961   48.589    0.000 1359.925    0.001 agent.py:172(__call__)
                2718970   46.511    0.000 1291.842    0.000 agent.py:112(__call__)
               13527079 1247.216    0.000 1247.216    0.000 {built-in method torch._C._nn.one_hot}
                8156901  187.079    0.000 1180.197    0.000 optimizer.py:189(zero_grad)
                3608535   39.481    0.000 1168.127    0.000 layers.py:849(restart)
             1048883631 1083.704    0.000 1083.704    0.000 layer.py:154(elements)
             4109014218  679.868    0.000  982.232    0.000 enum.py:646(__hash__)
              276445474  224.058    0.000  966.392    0.000 {built-in method builtins.any}
              271522144  551.682    0.000  880.127    0.000 layers.py:286(check)
               76131070  868.833    0.000  868.833    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3608535   18.225    0.000  845.539    0.000 level.py:8(__init__)
              271522144  486.766    0.000  819.125    0.000 layers.py:246(check)
               10808109  291.268    0.000  800.628    0.000 exploration.py:53(softmaxer)
               76131070  748.654    0.000  748.654    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             2414597085  614.219    0.000  742.334    0.000 layers.py:809(<genexpr>)
        11001628525/11001628522  665.909    0.000  740.690    0.000 {built-in method builtins.len}
                2718970   54.549    0.000  720.226    0.000 replaybuffer.py:18(stacker)
               76131070  718.049    0.000  718.049    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               76131070  716.093    0.000  716.093    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2718961   52.624    0.000  691.974    0.000 replaybuffer.py:63(stacker)
                3608535   72.798    0.000  659.970    0.000 levels.py:164(generate)
              210318630  634.350    0.000  634.350    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              271897100   73.204    0.000  590.474    0.000 {built-in method builtins.all}
                2718970  338.544    0.000  561.324    0.000 collector.py:46(collect)
               76131070  551.251    0.000  551.251    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              820120977  200.194    0.000  549.001    0.000 layers.py:799(<genexpr>)
                7217070   69.497    0.000  492.592    0.000 level.py:41(notUsed)
             5114504039  466.994    0.000  466.994    0.000 layer.py:99(positions)
              271522144  277.304    0.000  433.712    0.000 layers.py:313(check)
               12655010  163.856    0.000  431.895    0.000 random.py:315(sample)
              532917574  340.799    0.000  424.807    0.000 tensor.py:906(grad)
              271522144  270.263    0.000  419.878    0.000 layers.py:273(check)
                8156901   11.239    0.000  395.005    0.000 loss.py:527(forward)
                8156901   30.570    0.000  383.766    0.000 functional.py:2898(mse_loss)
              271522144  241.619    0.000  365.880    0.000 layers.py:48(check)
               59549658   37.926    0.000  342.866    0.000 flatten.py:39(forward)
               59549658  304.941    0.000  304.941    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             4109045273  302.368    0.000  302.368    0.000 {built-in method builtins.hash}
               87007032  290.985    0.000  290.985    0.000 layer.py:186(<listcomp>)
               21770894  288.719    0.000  288.719    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              271522144  183.475    0.000  274.332    0.000 layers.py:23(check)
               28868280   34.324    0.000  273.569    0.000 layer.py:77(restart)
              395165786  271.292    0.000  271.292    0.000 {built-in method torch._C._get_tracing_state}
               10808109  261.601    0.000  261.601    0.000 {built-in method multinomial}
                8156901  254.126    0.000  254.126    0.000 {built-in method torch._C._nn.mse_loss}
               87007032  247.510    0.000  247.510    0.000 layer.py:187(<listcomp>)
               13528789   20.861    0.000  242.733    0.000 tensor.py:525(__rsub__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9624189: <Causal3_Conver4_3counterfactsNOCRASH_2> in cluster <dcc> Done

Job <Causal3_Conver4_3counterfactsNOCRASH_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun May  9 01:29:17 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue May 11 03:14:26 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May 11 03:14:26 2021
Terminated at Wed May 12 03:09:41 2021
Results reported at Wed May 12 03:09:41 2021

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

    CPU time :                                   85898.27 sec.
    Max Memory :                                 8324 MB
    Average Memory :                             5828.03 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8060.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86226 sec.
    Turnaround time :                            265224 sec.

The output (if any) is above this job summary.


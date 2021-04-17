
# Parameters

    Name :                      cococonuts_CF_conver2-0
    Main :                      CFagent
    Level :                     Levels.Coconuts
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                2
    Counterfacts :              1
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      66989225409 function calls (66652083162 primitive calls) in 86117.53 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86117.533 86117.533 {built-in method builtins.exec}
                      1    5.128    5.128 86117.533 86117.533 <string>:1(<module>)
                      1  295.573  295.573 86112.405 86112.405 main.py:94(CFagent)
               11576031   50.394    0.000 28983.552    0.003 agent.py:29(learn)
               11576030  736.253    0.000 23410.895    0.002 learner.py:42(Qlearn)
                3858677   19.384    0.000 22527.019    0.006 game.py:41(step)
                3858677   23.802    0.000 21705.517    0.006 layers.py:710(step)
                3858677  391.769    0.000 15016.727    0.004 layers.py:17(step)
              385431863 1483.837    0.000 14584.836    0.000 layer.py:98(move)
        378097858/40957302 1591.596    0.000 12601.948    0.000 module.py:866(_call_impl)
               29381272   82.805    0.000 11737.139    0.000 network.py:24(forward)
               29381272  378.605    0.000 11449.798    0.000 container.py:117(forward)
                3858677  467.067    0.000 11285.005    0.003 agent.py:54(_learn)
                3858677  458.548    0.000 10328.374    0.003 agent.py:208(_learn)
               11576030  100.085    0.000 9060.464    0.001 optimizer.py:84(wrapper)
               11576030   54.534    0.000 8611.630    0.001 grad_mode.py:24(decorate_context)
              385431863 1001.921    0.000 8600.892    0.000 layers.py:727(check)
               11576030  372.045    0.000 8438.172    0.001 adam.py:55(step)
               11576030 1750.442    0.000 7661.452    0.001 _functional.py:53(adam)
                3858677  119.350    0.000 7289.990    0.002 agent.py:117(_learn)
                3858677  516.324    0.000 7094.241    0.002 agent.py:216(counterfact)
                3858678  589.004    0.000 6625.745    0.002 layers.py:676(update)
                3858677 4956.439    0.001 6321.428    0.002 replaybuffer.py:22(sample_data)
               11576030   49.460    0.000 6154.644    0.001 tensor.py:195(backward)
               11576030   49.303    0.000 6103.443    0.001 __init__.py:68(backward)
                8886266  254.027    0.000 5907.154    0.001 agent.py:49(__call__)
               11576030 5817.435    0.001 5817.435    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3858677 4385.379    0.001 5564.202    0.001 replaybuffer.py:49(sample_data)
                3858677 2786.051    0.001 4733.064    0.001 replaybuffer.py:28(teleporter_save_data)
                3858677 2079.800    0.001 4576.644    0.001 agent.py:88(interveen)
               58762544  137.980    0.000 4238.195    0.000 conv.py:398(forward)
               58762544   89.395    0.000 4029.805    0.000 conv.py:390(_conv_forward)
               54021485 2342.962    0.000 3968.883    0.000 layer.py:151(update)
               58762544 3940.410    0.000 3940.410    0.000 {built-in method conv2d}
               46539031 3707.648    0.000 3707.648    0.000 {built-in method tensor}
              385123639  613.940    0.000 3515.032    0.000 layers.py:721(isFree)
               37708239   22.800    0.000 3476.402    0.000 game.py:37(board)
              385431863 2394.771    0.000 3304.628    0.000 layers.py:464(check)
               80426462  169.763    0.000 3224.613    0.000 linear.py:93(forward)
               80426462   69.588    0.000 2961.060    0.000 functional.py:1737(linear)
             2579258142 2503.168    0.000 2901.092    0.000 layer.py:95(isFree)
                3858677 1901.802    0.000 2895.785    0.001 agent.py:67(modify)
               80426462 2875.170    0.000 2875.170    0.000 {built-in method torch._C._nn.linear}
              385431863 1906.985    0.000 2547.260    0.000 layers.py:71(check)
               55190385 2062.883    0.000 2062.883    0.000 {built-in method cat}
                3858676   76.146    0.000 1786.625    0.000 agent.py:167(__call__)
              181474295 1778.280    0.000 1778.280    0.000 {built-in method clone}
             6830365753 1244.607    0.000 1773.761    0.000 enum.py:646(__hash__)
                1778523   23.597    0.000 1720.997    0.001 layers.py:731(restart)
               12744943   85.776    0.000 1705.658    0.000 agent.py:59(modify_board)
              109807734   93.330    0.000 1693.777    0.000 activation.py:713(forward)
                3858677   70.137    0.000 1662.609    0.000 agent.py:112(__call__)
              109807734   94.065    0.000 1600.447    0.000 functional.py:1364(leaky_relu)
                1201623   26.557    0.000 1594.485    0.001 agent.py:171(choose_action)
                1778523   12.117    0.000 1509.060    0.001 level.py:8(__init__)
              109807734 1488.778    0.000 1488.778    0.000 {built-in method torch._C._nn.leaky_relu}
              216085892 1485.150    0.000 1485.150    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1778523   90.119    0.000 1405.122    0.001 levels.py:262(generate)
              216085892 1330.662    0.000 1330.662    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               11576030  238.887    0.000 1317.842    0.000 optimizer.py:189(zero_grad)
              387947955  312.517    0.000 1308.889    0.000 {built-in method builtins.any}
               22014358  201.864    0.000 1233.627    0.000 level.py:41(notUsed)
               12744943 1128.360    0.000 1128.360    0.000 {built-in method torch._C._nn.one_hot}
              385431863  862.750    0.000 1090.862    0.000 layers.py:56(check)
                3858677   87.648    0.000 1061.330    0.000 replaybuffer.py:18(stacker)
             3072714216  825.011    0.000  996.371    0.000 layers.py:692(<genexpr>)
             1079114190  956.400    0.000  956.400    0.000 layer.py:146(elements)
                3858676   77.655    0.000  890.036    0.000 replaybuffer.py:45(stacker)
              108042946  872.627    0.000  872.627    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              108042946  767.331    0.000  767.331    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              108042946  722.620    0.000  722.620    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              385867800  144.153    0.000  713.353    0.000 {built-in method builtins.all}
             7485271452  702.809    0.000  702.809    0.000 layer.py:91(positions)
              108042946  702.126    0.000  702.126    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              756300706  509.202    0.000  632.309    0.000 tensor.py:906(grad)
             1547762849  398.822    0.000  616.219    0.000 layers.py:682(<genexpr>)
                8886266  217.763    0.000  608.016    0.000 exploration.py:53(softmaxer)
                3858677  349.364    0.000  593.095    0.000 collector.py:53(collect)
                7717354  217.545    0.000  578.307    0.000 random.py:315(sample)
              385431863  391.616    0.000  571.060    0.000 layers.py:42(check)
        6890696262/6890696259  481.005    0.000  553.182    0.000 {built-in method builtins.len}
               22014358   25.254    0.000  548.259    0.000 level.py:38(elementsIn)
             6830409576  529.162    0.000  529.162    0.000 {built-in method builtins.hash}
                3858677  176.087    0.000  520.803    0.000 replaybuffer.py:55(CF_save_data)
               11576030   18.394    0.000  518.317    0.000 loss.py:527(forward)
              108042946  510.941    0.000  510.941    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               11576030   49.130    0.000  499.923    0.000 functional.py:2898(mse_loss)
               11576032  479.657    0.000  479.657    0.000 {built-in method nonzero}
              198077914  405.240    0.000  405.240    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              381696793  243.224    0.000  368.509    0.000 layer.py:126(remove)
               22014358  172.149    0.000  344.868    0.000 level.py:39(<listcomp>)
              982094204  320.371    0.000  320.371    0.000 level.py:32(inverse)
               11576030  304.754    0.000  304.754    0.000 {built-in method torch._C._nn.mse_loss}
              485815334  213.252    0.000  293.208    0.000 layer.py:130(add)
               11577303  285.768    0.000  285.768    0.000 {built-in method max}
               58762544   41.351    0.000  279.470    0.000 flatten.py:39(forward)
             2579258142  269.761    0.000  269.761    0.000 layer.py:203(isBlocking)
              411877584  177.341    0.000  264.392    0.000 random.py:250(_randbelow_with_getrandbits)
                1201623  239.488    0.000  255.271    0.000 agent.py:182(convert_values)
               23152062  254.181    0.000  254.181    0.000 {built-in method sum}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9501859: <cococonuts_CF_conver2_0> in cluster <dcc> Done

Job <cococonuts_CF_conver2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Apr  7 15:46:06 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Apr  7 16:08:09 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Apr  7 16:08:09 2021
Terminated at Thu Apr  8 16:03:38 2021
Results reported at Thu Apr  8 16:03:38 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
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

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85907.23 sec.
    Max Memory :                                 10691 MB
    Average Memory :                             6897.33 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               5693.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86129 sec.
    Turnaround time :                            87452 sec.

The output (if any) is above this job summary.

